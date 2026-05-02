# SD Low Cost Pager - Automatic Mode User Guide

## Overview

The automatic mode system continuously polls FTC Live for match queue changes and automatically notifies teams of their queue status via pagers. This guide explains how the system works, the key functions involved, and where to customize behavior.

## High-Level Flow

1. The user turns on automatic mode in `main.py`.
2. `toggle_automatic_mode()` starts a timer.
3. The timer repeatedly calls `poll_for_queue_changes()`.
4. `poll_for_queue_changes()` calls FTC Live through `ftclive_queueteams.py`.
5. The returned queue data is converted into a signature and compared with the previous poll.
6. If the queue changed, the system sends a yellow alert.
7. If the match state is `REVIEW`, the system sends a red alert and enters cooldown.
8. The UI is updated with match, team, and field information.

## Main.py Functions

### `toggle_automatic_mode(checked)`

Location: `main.py`

This function turns automatic mode on or off.

When enabled, it:
- Sets the polling interval.
- Resets the stored queue signature.
- Clears cooldown state.
- Starts the polling timer.
- Immediately runs one poll so the UI updates right away.
- Changes the automatic mode indicator to green.

When disabled, it:
- Stops the polling timer.
- Changes the automatic mode indicator to red.

Customization points:
- Change the polling interval in `self.poll_interval_ms = 30000`.
- Use a shorter interval for faster updates or a longer interval to reduce API load.

### `poll_for_queue_changes()`

Location: `main.py`

This is the main automatic polling loop.

What it does:
- Checks whether the system is in cooldown.
- Calls `get_active_match_details()` and `get_queue_match_details()` from `ftclive_queueteams.py`.
- If either request fails, it backs off for 60 seconds.
- Builds a queue signature from the returned match data.
- Extracts the queued team numbers and field number.
- Updates the UI with match number, teams, and field.
- Looks up pager IDs for the queued teams.
- Sends a yellow alert if the queue changed.
- Sends a red alert if the match is in `REVIEW`.

Customization points:
- Change the API failure cooldown at `self.api_cooldown_until = now + 60`.
- Change the review-state cooldown at `self.api_cooldown_until = now + 60` in the `REVIEW` block.
- Change the alert color hex values.
- Change the outgoing message text.
- Change when alerts are sent by adjusting the queue-change and match-state checks.

### `generate_queue_signature(queue_details)`

Location: `main.py`

This function creates a unique text signature for the current queued match using:
- match number
- red team 1
- red team 2
- blue team 1
- blue team 2

It is used to detect whether the queue has changed since the last poll.

Customization points:
- Usually none.
- If you want to compare different match data, change the fields that are concatenated into the signature.

### `extract_teams_from_queue(queue_details)`

Location: `main.py`

This function extracts the four team numbers from the queue response and returns them as a list of strings.

Returned order:
- red team 1
- red team 2
- blue team 1
- blue team 2

Customization points:
- Usually none.
- If the FTC Live response format changes, update the field paths here.

### `extract_match_state_from_queue(active_match_details)`

Location: `main.py`

This function returns the current match state from the active match response.

It is used to detect when the active match enters `REVIEW`.

Customization points:
- Change the match state comparison in `poll_for_queue_changes()` if you want alerts on a different state.
- Example: send alerts for `MATCH_OVER` or `QUEUED` depending on workflow.

### `extract_field_from_queue(queue_details)`

Location: `main.py`

This function extracts the field number from the queue response.

It is used when building the on-screen status display and the outgoing pager message.

Customization points:
- Usually none.
- Update the field path if the API response structure changes.

## ftclive_queueteams.py Functions

### `get_local_ip()`

This function discovers the local network IP address of the FTC Live host by opening a UDP socket and asking the OS which local address would be used.

Why it exists:
- It avoids hardcoding the FTC Live server IP.

Customization points:
- Hardcode `BASE_URL` if auto-detection is unreliable.
- Change the socket target if another address works better in your environment.

### `get_teams()`

This function sends a GET request to the FTC Live teams endpoint and returns the JSON payload.

It returns:
- the JSON response on success
- `None` on rate limit or error

Customization points:
- Change the request timeout.
- Add retry logic if needed.
- Modify error handling if you want more detailed diagnostics.

### `get_active_match_details()`

This function requests the active match endpoint from FTC Live.

It is the source for current match state and active match number.

Customization points:
- Change the timeout.
- Adjust error handling or add retries.

### `get_next_match_number()`

This function gets the currently active match number and adds 1 to determine the next queued match.

It also prevents match numbers above 80 from being used.

Customization points:
- Change the upper limit if your event format requires something different.
- Adjust the logic if FTC Live changes how queued matches are represented.

### `get_queue_match_details()`

This function uses `get_next_match_number()` to determine the next match, then requests the full match details from FTC Live.

This is the main source of queue data used by `poll_for_queue_changes()`.

Customization points:
- Change the request timeout.
- Change how the next match is determined.
- Modify the response handling if the API format changes.

## Module-Level Settings

### In `ftclive_queueteams.py`

- `EVENT_CODE`: FTC Live event number.
- `BASE_URL`: Auto-detected local IP address for the FTC Live server.
- `teams_url`: Endpoint used to fetch team numbers.
- `active_match_url`: Endpoint used to fetch the active match.

Common adjustments:
- Change `EVENT_CODE` when switching events.
- Replace `BASE_URL = get_local_ip()` with a fixed IP if needed.

### In `main.py`

- `self.poll_interval_ms`: Polling frequency in milliseconds.
- `self.api_cooldown_until`: Timestamp for cooldown after API problems or review-state messages.
- `self.last_queue_signature`: Stores the previous queue state so changes can be detected.

Common adjustments:
- Lower `self.poll_interval_ms` for faster notifications.
- Increase cooldowns to reduce API calls.
- Change the alert colors used for queue changes and review state.

## Common Customization Scenarios

### Make polling faster

Change:
- `self.poll_interval_ms = 30000`

Example:
- `self.poll_interval_ms = 15000`

### Make cooldown longer

Change:
- `self.api_cooldown_until = now + 60`

Example:
- `self.api_cooldown_until = now + 120`

### Change queue-change alert color

Change:
- `intensity = "FFFF00"`

Examples:
- `"00FF00"` for green
- `"0000FF"` for blue

### Change review-state alert color

Change:
- `intensity = "FF0000"`

Examples:
- `"FFFF00"` for yellow
- `"FFFFFF"` for white

### Change the message text sent to teams

Change the strings in `poll_for_queue_changes()`.

Examples:
- `red team head to arena {field_num}`
- `blue team head to arena {field_num}`

### Send alerts for more states

Change the condition in `poll_for_queue_changes()`.

Current:
- `if match_state == "REVIEW":`

Possible alternatives:
- `if match_state in ["REVIEW", "MATCH_OVER"]:`
- `if match_state != "QUEUED":`

## Notes on Behavior

- `ftclive_queueteams.py` runs API calls at import time for the team-number download block.
- If FTC Live is unavailable, the guard around `teamNumbers` prevents a crash, but the app still depends on valid API responses for automatic mode.
- The team-number list is used later when mapping queued team numbers to pager IDs in `main.py`.

## Quick Reference

| Function | Purpose |
| --- | --- |
| `toggle_automatic_mode()` | Starts or stops automatic polling |
| `poll_for_queue_changes()` | Polls FTC Live, updates UI, and sends alerts |
| `generate_queue_signature()` | Detects queue changes |
| `extract_teams_from_queue()` | Extracts queued team numbers |
| `extract_match_state_from_queue()` | Gets current match state |
| `extract_field_from_queue()` | Gets queue field number |
| `get_local_ip()` | Finds the local FTC Live server IP |
| `get_teams()` | Fetches event team numbers |
| `get_active_match_details()` | Fetches active match details |
| `get_next_match_number()` | Determines the next queued match |
| `get_queue_match_details()` | Fetches full details for the next queued match |

