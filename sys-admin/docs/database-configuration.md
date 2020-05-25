# TACTIC Database Configuration

TACTIC supports a variety of database types, including,

- PostgreSQL
- MySQL
- SQLServer
- SQLite

The database connection is configured in the TACTIC configuration file.
See Configuration Directives > Database for configuration of the TACTIC database connection.


## Change Databases

By default TACTIC will look at localhost to the database. This is the
simplest implementation and most installations will have the database on
the same physical server as the TACTIC application servers. However, in
scaling up TACTIC, it may become necessary to separate the database
server from the TACTIC applications servers.

## Editing the TACTIC config file

TACTIC can be configured to look at an external database by connecting
through sockets of TCP/IP. This can be set in the TACTIC configuration
file. This file is located here:

    <TACTIC_DATA_DIR>/config/tactic-conf.xml

The <database> section configures the database.  An example configuration is shown below:

    <!-- database -->
    <database>
        <vendor>PostgreSQL</vendor>
        <server>localhost</server>
        <port>5432</port>
        <user>postgres</user>
        <password>none</password>
    </database>

For details on these settings, you can look at the [configuration](configure-tactic/#database) documentation.

## Command Line Usage

While it is possible to edit this file manually, it is often simpler to
use the provided utility found in:

    <TACTIC_INSTALL_DIR>/src/bin/util/change_db_info.py

This command line script will ask a series of questions and update the appropriate configuration file.

    python change_db_info.py

When executing, the script will ask configuration questions and show a
default value in brackets. If the default is sufficient, merely press
enter without entering anything in will accept the default.

Below is a sample output where all the default values are accepted:

## TACTIC Database Configuration

    Please enter the database vendor (PostgreSQL or Oracle):

    (PostgreSQL) →

    Please enter database server hostname or IP address:

    (localhost) →

    Please enter user name accessing the database:

    (postgres) →

    Please enter database password:

    (ENTER to keep password, '*EMPTY*' for empty password)

    Enter Password →

    Vendor: [PostgreSQL]

    Server: [localhost]

    User: [postgres]

    Save to config (N/y) →

Once the values have been saved, a restart of TACTIC is required to
start using the new database configuration.




