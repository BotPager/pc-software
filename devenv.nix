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
  packages = with pkgs; [
    # Mehtastic CLI and library
    meshtastic
    # is currently broken in nixpkgs and also unmaintained
    # meaning running the script will work and qt creator will load and .ui can be changed
    # however regenerating PCUI.py will not work as uic-pyside6
    # refrence 
    # author reccomends setting up at distrobox
    python3Packages.pyside6
    # System dependencies often needed for Qt/PySide applications
    qt6.qtbase
    #qt design app
    qtcreator
    #numpy for creating csv
    python3Packages.numpy
  ];

  # See full reference at https://devenv.sh/reference/options/
}

