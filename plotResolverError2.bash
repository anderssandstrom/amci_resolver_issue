bash ~/sources/fat_sat_tools/report/reportMainTest.bash report_resovertest.cfg ~/sources/ecmc_bifrost_slits_sat/tests_2/11358/axis1/data.log ~/temp.md | grep IOC_TEST | head -n 9200 | tail -n 9000 |python ~/sources/amci_resolver_issue/plotReolverError.py