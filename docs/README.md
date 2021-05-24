
<p align="center"><img src="/media/ida_migrator.png" width=700 height=200></p>

# IDA Migrator Plugin

IDA Migrator plugin aids migrating function names, structures and enums from one database instance to another.

This comes in handy when:
* Moving to a newer version of IDA that does better analysis and you don't want to change in the new instance type information or variable names of the decompiled functions.
* The current idb instance fails to decompile a function or the decompilation looks wrong in comparison to another idb instance of the same binary.
* Experimenting on another idb instance before making major changes on the current instance.
* A lightweight easy way of creating small incremental backups from the current work.
* For w/e reason, the current idb instance you're working on gets corrupted.


IDA Migrator plugin developed using PyQt, hence should work on all platforms.

## Getting Started

Download links can be found [here](https://github.com/giladreich/ida_migrator/releases).

Copy the files under the `source` directory and put them under your IDA installation `plugins` directory.

Start your current IDA instance you want to migrate from and then press `CTRL+SHIFT+D` to show the plugin's UI. Alternative; open it through the `Edit -> Plugins -> IDA Migrator` menu:

![Intro](/media/intro.png)


### Step 1 - Exporting Data

Clicking the `Export` button will show all functions of the current database instance:

![Exporter UI](/media/exporter_1.png)

Hint: You can uncheck any functions you want to exclude from exporting.

Once you click the `Start Export` button, it will ask you where would you like to export the files; One is the `*symbols*.json` storing addresses and function names and the other is `*types*.idc` having all the structures and enums information:

![Exporter Files](/media/exporter_2.png)


### Step 2 - Importing Data

In the new idb instance, open the plugin again and click on the `Import` button, which will then ask you to provide the `*symbols*.json` file:

![Importer UI](/media/importer_1.png)

Same procedure from here, just that once you click the `Start Import` button, it will ask you if you would like to import structures and enums as well from the exported `*types*.idc` file, that's optional for you to choose.

Note that it will only rename functions that does not have the same name and will output what functions has been affected in IDA's console:

![Importer Results](/media/importer_2.png)


## Contributing

Pull-Requests are greatly appreciated should you like to contribute to the project.

Same goes for opening issues; if you have any suggestions, feedback or you found any bugs, please do not hesitate to open an [issue](https://github.com/giladreich/ida_migrator/issues).

## Authors

* **Gilad Reich** - *Initial work* - [giladreich](https://github.com/giladreich)

See also the list of [contributors](https://github.com/giladreich/ida_migrator/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

