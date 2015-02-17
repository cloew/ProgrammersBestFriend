from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig('open', 'pbf.Commands.open.Open', description="Open the provided file in the default editor."),
            CommandConfig('insert pbf-package', 'pbf.Commands.PBF.insert_pbf_package.InsertPbfPackage', description="Insert a PBF Package into the Properties file"),
            CommandConfig('install tab-completion', 'pbf.Commands.PBF.install_tab_completion.InstallTabCompletion', description="Install the PBF Tab Completion")]

RegisterCommands(commands)