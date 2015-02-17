from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig('open', 'pbf.Commands.open.Open', description="Open the provided file in the default editor."),
            CommandConfig('insert pbf-package', 'pbf.Commands.PBF.insert_pbf_package.InsertPbfPackage', description="Insert a PBF Package into the Properties file"),
            CommandConfig('install tab-completion', 'pbf.Commands.PBF.install_tab_completion.InstallTabCompletion', description="Install the PBF Tab Completion"),
            CommandConfig('new pbf-properties', 'pbf.Commands.PBF.new_pbf_properties.NewPbfProperties', description="Creates a new empty PBF Properties file"),
            CommandConfig('new project', 'pbf.Commands.Project.new_project.NewProject', description="Create a new PBF Project"),
            CommandConfig('project open', 'pbf.Commands.Project.open_project_file.OpenProjectFile', description="Open a file within the currrent project")]

RegisterCommands(commands)