Upgrade Notice
==============

If you upgrade an existing Minerals block explorer to Mineralscoin, you need to run a few additional commands:

Change to your Minerals-abe installation directory and issue:

    sudo service apache2 stop

    sudo rm -r build/* 

    mysql <abe db> -u <user> -p

Search for your former Minerals chain:

```mysql> select * from chain;
+----------+--------------+-------------+-----------------------+------------------------+-------------+--------------+----------------+---------------------+
| chain_id | chain_name   | chain_code3 | chain_address_version | chain_script_addr_vers | chain_magic | chain_policy | chain_decimals | chain_last_block_id |
+----------+--------------+-------------+-----------------------+------------------------+-------------+--------------+----------------+---------------------+
|       15 | Minerals     | MIN         | 2                     |                        | ����        | Minerals     |           NULL |             1505350 |
+----------+--------------+-------------+-----------------------+------------------------+-------------+--------------+----------------+---------------------+
1 row in set (0.00 sec)```

Update Minerals to Mineralscoin:

    update chain SET chain_name="Mineralscoin", chain_policy="Mineralscoin" WHERE chain_id=15;

    quit

    sudo python setup.py install

    sudo service apache2 restart

Congratulations. You've just upgraded from Minerals to Mineralscoin.