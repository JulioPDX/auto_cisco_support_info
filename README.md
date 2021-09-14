# Cisco Support Info

This repo uses Nornir, NAPALM, and Cisco support APIs to gather device information and construct a CSV file with relevant information. Please see example CSV below.

|Name           |Platform|Model         |Base_PID         |Replacement    |Serial     |EoS       |EoSM      |LDoS      |EoCR      |Manufacture Year|Current SW          |
|---------------|--------|--------------|-----------------|---------------|-----------|----------|----------|----------|----------|----------------|--------------------|
|some-router-01 |Cisco   |ASR1001-HX    |ASR1001-HX       |N/A            |ZZZ21390123|N/A       |N/A       |N/A       |N/A       |2017            | Version 17.3.3     |
|some-other-node|Cisco   |WS-C3750E-48TD|WS-C3750E-48TD-SD|WS-C3750X-48T-S|ZZZ1419P0ZZ|2013-01-30|2014-01-30|2018-01-31|2017-04-30|2010            | Version 12.2(53)SE2|
|some-router-02 |Cisco   |ASR1001-HX    |ASR1001-HX       |N/A            |ZZZ21410012|N/A       |N/A       |N/A       |N/A       |2017            | Version 17.3.3     |
