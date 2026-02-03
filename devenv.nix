{
  pkgs,
  lib,
  config,
  ...
}:
{
  # https://devenv.sh/languages/
  languages = {
    python = {
      enable = true;
      venv.enable = true;
    };
  };

  # https://devenv.sh/packages/
  packages = [
    # Mehtastic CLI and library
    pkgs.meshtastic
    # PySide6 requirements
    pkgs.python3Packages.pyside6
    # System dependencies often needed for Qt/PySide applications
    pkgs.qt6.qtbase
  ];

  # See full reference at https://devenv.sh/reference/options/
}

