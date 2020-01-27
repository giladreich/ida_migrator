
<p align="center"><img src="images/ida_migrator.png" width=700 height=200></p>

# IDA Migrator Plugin

IDA Migrator plugin makes the job of migrating symbols and type informations from one IDA database instance to another. It will help migrating function names, structures and enums.

This comes in handy when:
* Moving to a newer version of IDA that does better analysis and you don't want to change in the new instance type information or variable names of the decompiled functions.
* The current idb instance fails to decompile a function or the decompilation looks wrong in comparison to another idb instance of the same binary.
* Experimenting on another idb instance before making major changes on the current instance.
* A lightweight easy way of creating small backups of the current work.
* For w/e reason, the current idb instance you're working on gets corrupted.


IDA Migrator plugin developed using PyQt, hence should work on all platforms.

## Getting Started

Download links can be found [here](https://github.com/giladreich/ida_migrator/releases).

Copy the files under the `src` directory and put them under IDA installation `plugins` directory.

Start your current IDA instance you want to migrate from and then press `CTRL+SHIFT+D` to start the plugin. Alternative; open it through the `Edit -> Plugins -> IDA Migrator` menu:

![Intro](/images/intro.png)


### Step 1 - Exporting Data

Click the `Export` button to load current instance functions:

![Exporter UI](/images/exporter_1.png)

Hint: You can uncheck any functions you don't want to be exported.

Once you click the `Start Export` button, it will ask you where would you like to export the files; One is the `*symbols*.json` storing addresses and function names and the other is `*types*.idc` having all the structures and enums information:

![Exporter Files](/images/exporter_2.png)


### Step 2 - Importing Data

In the new idb instance, open the plugin again and click on the `Import` button, which will then ask you to provide the `*symbols*.json` file:

![Importer UI](/images/importer_1.png)

Same procedure from here, just that once you click the `Start Import` button, it will ask you if you would like to import structures and enums as well from the exported `*types*.idc` file, so it's up to you to decide.

Note that it will only rename functions that does not have the same name and will output what functions has been affected:

![Importer Results](/images/importer_2.png)


## Contributing

Pull-Requests are greatly appreciated should you like to contribute to the project. 

Same goes for opening issues; if you have any suggestions, feedback or you found any bugs, please do not hesitate to open an [issue](https://github.com/giladreich/ida_migrator/issues).

## Authors

* **Gilad Reich** - *Initial work* - [giladreich](https://github.com/giladreich)

See also the list of [contributors](https://github.com/giladreich/ida_migrator/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

