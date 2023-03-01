# Enchantments Lottery Permit Probability

**Author**: Eric Kennedy

## Calculate odds of getting a permit by start date selected

Lottery applicants can enter a first, second and third choice for both a date and a zone.

The Core Enchantments Zone is the most competitive as only 16 spots are normally available. 
Due to Covid restrictions, an additional 8 spots were available for entries on Sunday in 2020-2022.
It appears those extra spots will be available in 2023.

View [map with applications per zone](https://www.fs.usda.gov/Internet/FSE_DOCUMENTS/fseprd568443.pdf)

Data from [fs.usda.gov](https://www.fs.usda.gov/detail/okawen/passes-permits/recreation/?cid=fsbdev3_053607)

```
              weekday r1_winners r1_entries  r1_odds r2_winners r2_entries  r2_odds r3_winners r3_entries  r3_odds
entry_date                                                                                                        
2022-10-23     Sunday          4          4   100.0%          0          0                   0          0         
2022-10-16     Sunday         20         30    66.7%          0         36     0.0%          4         33    12.1%
2022-10-21     Friday          8         16    50.0%          0          8     0.0%          8         68    11.8%
2022-10-09     Sunday         21         72    29.2%          0         93     0.0%          3        114     2.6%
2022-10-18    Tuesday          7         25    28.0%          0          2     0.0%          9         57    15.8%
2022-10-12  Wednesday         11         85    12.9%          5         61     8.2%          0        139     0.0%
2022-10-02     Sunday         20        229     8.7%          0        256     0.0%          4        241     1.7%
2022-10-11    Tuesday          4         58     6.9%         12         96    12.5%          0        116     0.0%
2022-06-19     Sunday         16        311     5.1%          0        158     0.0%          8        148     5.4%
2022-06-26     Sunday         22        432     5.1%          2        240     0.8%          0        128     0.0%
2022-07-03     Sunday         24        499     4.8%          0        306     0.0%          0        167     0.0%
2022-09-27    Tuesday         16        374     4.3%          0        369     0.0%          0        382     0.0%
2022-06-22  Wednesday         15        362     4.1%          0        244     0.0%          0        188     0.0%
2022-10-15   Saturday          4         97     4.1%          6        169     3.6%          6        142     4.2%
2022-09-18     Sunday         15        384     3.9%          6        437     1.4%          3        531     0.6%
2022-10-04    Tuesday          8        207     3.9%          2        325     0.6%          6        406     1.5%
2022-06-15  Wednesday         12        330     3.6%          0        117     0.0%          4        126     3.2%
2022-06-16   Thursday         15        421     3.6%          1        286     0.3%          0        198     0.0%
2022-10-13   Thursday          4        116     3.4%          0        105     0.0%         12        275     4.4%
2022-09-11     Sunday         24        710     3.4%          0        554     0.0%          0        659     0.0%
2022-10-06   Thursday         15        448     3.3%          0        430     0.0%          1        671     0.1%
2022-07-10     Sunday         18        540     3.3%          0        349     0.0%          6        223     2.7%
2022-09-28  Wednesday         14        423     3.3%          2        507     0.4%          0        687     0.0%
2022-06-21    Tuesday         10        322     3.1%          0        214     0.0%          6         98     6.1%
2022-09-20    Tuesday         16        520     3.1%          0        639     0.0%          0        649     0.0%
              weekday r1_winners r1_entries  r1_odds r2_winners r2_entries  r2_odds r3_winners r3_entries  r3_odds
entry_date                                                                                                        
2021-10-20  Wednesday          7          7   100.0%          0          3     0.0%          8         35    22.9%
2021-10-24     Sunday          2          2   100.0%          4          4   100.0%         15         15   100.0%
2021-10-18     Monday          8         14    57.1%          0         21     0.0%          8         35    22.9%
2021-10-23   Saturday          9         25    36.0%          0         15     0.0%          6         22    27.3%
2021-10-13  Wednesday         16         54    29.6%          0        137     0.0%          0        209     0.0%
2021-10-10     Sunday          9         87    10.3%          4         79     5.1%         10        148     6.8%
2021-10-16   Saturday          4         41     9.8%          6         44    13.6%          6        150     4.0%
2021-10-03     Sunday         18        195     9.2%          0        189     0.0%          6        198     3.0%
2021-06-20     Sunday         24        264     9.1%          0         81     0.0%          0        126     0.0%
2021-06-27     Sunday         18        206     8.7%          6        167     3.6%          0        132     0.0%
2021-10-14   Thursday          6         74     8.1%          4         63     6.3%          6        178     3.4%
2021-06-29    Tuesday         12        226     5.3%          2        255     0.8%          2        153     1.3%
2021-10-06  Wednesday         15        294     5.1%          1        286     0.3%          0        404     0.0%
2021-10-11     Monday          6        118     5.1%          8        137     5.8%          2        146     1.4%
2021-10-17     Sunday          1         20     5.0%         11         31    35.5%         12         32    37.5%
2021-10-09   Saturday          6        123     4.9%          0        189     0.0%         10        331     3.0%
2021-06-15    Tuesday         12        248     4.8%          4        181     2.2%          0         95     0.0%
2021-10-12    Tuesday          4         92     4.3%         10         85    11.8%          2        102     2.0%
2021-09-05     Sunday         24        566     4.2%          0        536     0.0%          0        505     0.0%
2021-06-30  Wednesday         16        378     4.2%          0        269     0.0%          0        294     0.0%
2021-09-29  Wednesday         11        307     3.6%          5        376     1.3%          0        458     0.0%
2021-06-22    Tuesday         13        363     3.6%          2        188     1.1%          0        128     0.0%
2021-09-19     Sunday         14        410     3.4%          0        419     0.0%         10        486     2.1%
2021-07-11     Sunday         20        586     3.4%          4        291     1.4%          0        256     0.0%
2021-06-21     Monday         14        414     3.4%          0        228     0.0%          2        206     1.0%
              weekday r1_winners r1_entries  r1_odds r2_winners r2_entries  r2_odds r3_winners r3_entries  r3_odds
entry_date                                                                                                        
2020-10-21  Wednesday          2          2   100.0%         12         16    75.0%          2         10    20.0%
2020-10-25     Sunday         12         12   100.0%          0          0                   0          0        
2020-10-18     Sunday         12         12   100.0%          4          8    50.0%          6         10    60.0%
2020-10-20    Tuesday         10         10   100.0%          2          6    33.3%          4         16    25.0%
2020-10-24   Saturday         12         16    75.0%          2          6    33.3%          2         10    20.0%
2020-10-19     Monday          6         10    60.0%          6          6   100.0%          4          8    50.0%
2020-10-22   Thursday          8         16    50.0%          8         16    50.0%          0         12     0.0%
2020-10-11     Sunday         14         30    46.7%          0         36     0.0%         10         38    26.3%
2020-10-14  Wednesday          8         40    20.0%          2         30     6.7%          6         26    23.1%
2020-10-04     Sunday         20        116    17.2%          4         96     4.2%          0        112     0.0%
2020-09-27     Sunday         23        163    14.1%          0        108     0.0%          0        196     0.0%
2020-09-30  Wednesday         14        114    12.3%          0        236     0.0%          2        206     1.0%
2020-10-23     Friday          1          9    11.1%          4         24    16.7%         10         50    20.0%
2020-09-29    Tuesday         12        108    11.1%          0        128     0.0%          4        208     1.9%
2020-09-20     Sunday         24        224    10.7%          0        172     0.0%          0        324     0.0%
2020-07-05     Sunday         22        222     9.9%          2        106     1.9%          0         88     0.0%
2020-10-05     Monday         16        164     9.8%          0        132     0.0%          0        164     0.0%
2020-10-15   Thursday          4         44     9.1%          2         58     3.4%         10         66    15.2%
2020-10-06    Tuesday          8         92     8.7%          0        112     0.0%          8        120     6.7%
2020-10-16     Friday          5         61     8.2%          0        100     0.0%         11        123     8.9%
2020-09-28     Monday         11        143     7.7%          0        164     0.0%          5        181     2.8%
2020-10-12     Monday          3         39     7.7%          8         44    18.2%          4        104     3.8%
2020-06-17  Wednesday         16        216     7.4%          0        108     0.0%          0         56     0.0%
2020-06-28     Sunday         11        159     6.9%         13        153     8.5%          0        128     0.0%
2020-06-30    Tuesday         16        236     6.8%          0        140     0.0%          0        104     0.0%
```