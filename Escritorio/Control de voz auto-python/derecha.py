import numpy as np

derecha = [[ 11.79857305 , 10.78136662,  14.43544226,  16.25347097,  15.62338021
   ,11.77940849,  12.47388277,  13.13490828,  14.75100406,  16.01170551
   ,14.65241545,  14.3044933,   12.71735134,  13.70022749,  14.16538092
   ,10.44357991,  11.2284515,   11.96379783,  11.44517557,  10.87838377
   ,10.71207694,  11.21078668,  11.13868572,  10.6848091,  10.38226541
   ,10.88924389],
 [ 13.33368586,  14.4001207,   14.46593011,  16.59916651,  16.2600388
   ,13.78807803,  12.43059144, 12.77815103,  14.83484223,  15.91128632
   ,15.16152855,  14.600471,    13.01804298,  14.0278023,   14.43527515
   ,12.02691558,  11.85376681,  11.72093282,  11.30941158, 11.03187606
   ,10.6453857,   11.07508505,  11.21938844,  10.93654907,  10.61968951
   ,10.91236611],[  9.83098196,  11.19110262,  14.13778206,  16.3703484,   15.23289351
   ,12.86931172,  12.24340327,  12.96580047,  14.56837817,  16.79336174
   ,15.53051223,  14.22135923,  13.28315549,  13.98810633,  15.61287794
   ,13.37374461,  13.87130336,  13.66636887,  13.05963042,  12.65524204
   ,12.63635527,  13.11174709,  13.10901297,  12.63271393,  12.58628994
   ,13.13716774],
 [ 13.13511934,  13.03807281,  14.63109178,  17.14727145,  15.89527118
   ,14.07230152,  12.32651076,  13.05268862,  14.65069774,  16.09247385
   ,15.34482538,  13.97120148,  13.52813633,  14.25596401,  16.28515241
   ,14.69744217,  14.82207762,  14.48157792,  13.11931373,  13.12441804
   ,12.89175528,  13.14045464,  13.26766402,  12.92039735,  12.82948966
   ,13.0567896 ],[ 11.68041839,   9.71396321,  13.23864282,  16.50271893,  13.89919198
   ,12.16967454,  11.82266736,  12.23054838,  13.75701721,  16.53070424
   ,13.96736309,  14.10201613,  13.32598985,  14.01655009,  14.93791958
   ,11.58061276,  12.98993888,  13.33920159,  12.46513697,  12.31073884
   ,12.12507526,  12.60282957,  12.33955629,  12.05687043,  12.22024567
   ,12.58942645],
 [ 10.95258782,  11.26454528,  13.45945865,  15.73369152,  14.87661265
   ,13.42829553,  13.68872707,  13.68040647,  14.0413298,   16.42451593
   ,14.00078937,  13.65596613,  13.17751656,  14.36759817,  15.1205957
   ,12.92332498,  13.34447764,  13.24358409,  12.39647227,  11.97614626
   ,12.23846224,  12.56166251,  12.5146618,   12.2723214,  12.27912961
   ,12.63334873],[ 12.35350512, 14.17254704,  14.8894275,   17.29692611,  15.02373105
   ,13.53695282,  13.95272743,  14.14096282,  14.8974412,   16.64833652
   ,15.84994922,  14.87684104,  14.23957574,  14.55417544,  15.17384119
   ,12.24361054,  13.17092771,  13.22573997,  12.7667479,   12.25050193
   ,12.62850948,  13.22697617,  13.19492654,  12.89855295,  12.92935927
   ,13.20264537],
 [ 11.8313894,   13.66632721,  14.76598023,  17.72679931,  15.54115289
   ,13.58302922,  12.95763158,  12.63879799,  14.39827176,  16.91261869
   ,16.42573789,  15.4787877,   14.54966803,  14.47372178,  15.8614461
   ,12.50197943,  13.36742086,  12.89339899,  12.67879773,  12.21941883
   ,12.46357943,  13.06972303,  13.28273762,  12.91236964, 12.68900706
   ,13.10375897],[ 11.2265273,   13.16428411,  14.87818391,  17.37468737,  16.27129801
   ,13.86377897,  12.98243578,  12.61244793,  14.42505818,  16.36532698
   ,15.51283262,  13.8881148,   13.12975451,  14.41423712,  15.55359233
   ,13.11501395,  13.67928368,  14.26918428,  13.05100174,  11.95084405
   ,12.28138891,  12.81191672,  12.75352179,  12.36450663,  12.55538687
   ,13.12664166],
 [ 14.22672576,  15.12013689,  15.6068947,   17.63542543,  16.25939009
   ,13.86447376,  14.05611048,  13.96240748, 14.29037559,  15.7986893
   ,15.59496113,  13.96464316,  13.0007856,   14.41085435, 15.44386079
   ,13.50389654,  13.9293118,   13.60635594,  12.46325418,  11.61702191
   ,12.53545301,  12.9161269,   12.89928456,  12.53076638,  12.49848092
   ,12.68520684],

[  9.86898862 , 12.52821739  ,13.76684671 , 15.70958688  ,14.28920657,
   12.53245164,  11.74274033 , 11.71822028,  13.68226828 , 16.60588438,
   15.31984874,  16.67428197  ,15.34349966 , 13.66329728 , 14.05017567,
   11.14556162 , 10.73729955  ,10.78630619,  11.00431569 , 11.13738732,
   11.39618362,  11.75755141  ,11.83665068,  11.5496729  , 11.65315393,
   11.91486124],
 [ 10.92699652 , 10.22950723 , 13.51535191,  16.15232605,  14.96990926,
   13.39562594 , 13.15010388 , 13.16124091,  14.51641427,  16.37936617,
   15.83503228  ,16.63578552 , 16.17190735,  13.92168765,  14.12849498,
   11.51734673  ,11.00177996 ,  9.94305277,  10.47905578,  10.83043912,
   11.59027339  ,11.97754654  ,11.98128816,  11.69040474,  11.48025453,
   11.72180595],

[  9.78543372,  12.50846071 , 13.76095539  ,15.83967533 , 14.77151789,
   13.3902543,   12.96648746,  13.05427305 , 14.32835575,  16.65097433,
   15.4555515 , 16.97563622 , 16.09952429  ,14.64085216 , 14.58174306,
   11.73534819,  11.01314304,  10.16706818 , 10.42089279,  10.48061317,
   11.27757426,  11.7958244  , 11.6860934  , 11.37413181,  11.35351242,
   11.94734356],
 [ 11.14269109 , 10.70516829  ,13.72214022,  16.10978594 , 15.26726961,
   13.82294082 , 13.16237982  ,12.78555033,  14.43743837 , 17.17162047,
   17.08002815 , 17.93591013  ,17.6041239 ,  15.1387295  , 15.11007231,
   11.96412205 , 11.23279643  ,10.11902189,  10.51244705 , 10.96366573,
   11.31175661,  11.73991033  ,11.53392258,  11.4513746   ,11.6045892,
   11.77033608],
[ 10.28147938  ,12.37444011  ,13.40973268  ,15.41366207  ,14.27559497,
   12.53350895 , 11.81486768,  11.53762558 , 12.76058565 , 15.09543746,
   15.21024571 , 15.0117357  , 15.20307243 , 12.32566274 , 11.21031867,
   10.32700372 ,  9.93782993,   9.58498709 , 10.15567839 , 10.50442535,
   11.0521836  , 11.53574992,  11.34385021 , 11.01320336 , 11.18120891,
   11.54692389],
 [ 10.0695173  ,  7.58120349 , 12.84008549 , 15.36124277,  14.47565683,
   12.94267505 , 12.51162731 , 11.82790352 , 12.70547118,  14.72057284,
   14.88962254 , 14.60872777 , 14.80119294 , 12.39540543,  11.35045337,
    9.78401334 ,  9.8786941  ,  8.71908448  ,10.24059235,  10.42753574,
   11.05174622,  11.54127315 , 11.41022298  ,11.18141   ,  11.28494036,
   11.50083331],
[ 11.98390098 , 12.37053512 , 13.89143664 , 15.30966135  ,14.20713298,
   12.23595298,  11.13344739,  11.22755036,  12.95592894 , 15.45309169,
   14.87707369 , 15.44045539,  15.25020835,  12.46547716 , 11.59200049,
   10.19158773 , 10.42899182,   9.74332754,  11.34399795 , 12.14784008,
   11.85448027 , 11.95945632,  12.13352466,  11.73961897 , 11.52748647,
   12.1120694 ],
 [ 11.17172092 ,  8.61865079 , 13.73252095,  15.65874124 , 14.5846848,
   12.53424159 , 11.19184284 , 11.44296051,  12.93431124 , 14.44600234,
   14.9211596  , 15.07435056  ,14.98434717,  12.56891265 , 12.2981789,
   10.45633344 , 10.28476747 ,  9.77190759,  11.29879896 , 13.13786923,
   12.86629972 , 12.37907317 , 12.23852861,  12.03040316 , 12.09348439,
   12.06282245],
  [ 12.19252912,  12.54337142,  13.88783991,  15.18671257,  14.36662288,
   11.99897512 , 10.2999413  , 11.50570961 , 13.33473896 , 15.76712217,
   15.09212581 , 15.87770695  ,15.32678968 , 12.90801294  ,12.29614778,
   10.43126219 ,  9.83644208 ,  9.36739529 , 10.23572403  ,10.57214998,
   11.38108655 , 11.9368675  , 11.82026699 , 11.31132962  ,11.2465632,
   11.53965255],
 [  9.31080557,  10.90695893,  13.57841674 , 15.69381887 , 14.7579823,
   12.4514689 ,  10.69659887,  11.28156438 , 13.26834567 , 15.60481825,
   15.29893506 , 16.01884484,  15.65881543 , 13.26363553 , 12.53162669,
   10.66130941 , 10.0504293 ,   9.81713037 , 10.28879124,  10.73132555,
   11.38255724 , 11.72425286 , 11.77321084 , 11.41719858,  11.11236215,
   11.48854031],[ 11.30070809,  11.40758424  ,13.47030176 , 13.10373195 , 11.25128281
   ,11.94891949 , 12.4841847 ,  12.20891204 , 13.71659473 , 14.57533582
   ,13.78797261 , 13.73837644 , 13.12322415,  13.16191075,  13.24809342
   ,12.19765666 , 13.41356629 , 12.58230225,  13.63268581,  13.69263586
   ,14.24672693 , 14.83790878 , 14.75483551,  14.31188086,  14.26438033
   ,14.85607407],
 [ 11.39530734 , 11.41269963 , 13.67786962 , 15.89373318,  13.33441967
   ,11.85330608 , 12.65377351 , 11.87677531  ,13.8829425 ,  15.17446828
   ,13.51117307 , 14.39483787 , 13.74494097, 12.18338132 , 13.14306903
   ,12.49210946 , 13.12664394 , 12.90590097 , 13.25079718,  13.87539111
   ,14.29610045 , 14.86441137 , 14.84902652 , 14.57830076,  14.38312861
   ,15.03950886],[ 10.47136702,  11.23629839,  11.03469126,   9.32686193,   9.18270632
    ,8.51482744 ,  9.12882678 ,  9.55426659 ,  9.09927592 ,  8.50854639
    ,9.10572844 ,  9.4523712  , 10.27526485 ,  9.98860116 , 10.82286212
   ,12.04388325 , 13.12990629 , 11.47541863 , 13.26168527 , 13.44239238
   ,14.05655515 , 14.66771064 , 14.93462702 , 14.41769891 , 14.20091936
   ,14.68778861],
 [  8.17457408 ,  9.68427466 ,  8.5709085  , 10.01043747,   9.62348603
    ,7.71081847 ,  9.40881237 ,  9.57309277 ,  8.86521307 ,  8.73860014
   , 9.29286236 ,  8.70752214 ,  9.9211656  , 10.14068133 , 10.97482326
   ,12.26676429 , 13.10126353 , 11.64012029 , 13.33342345 , 13.65869855
   ,13.99674252 , 14.55281651 , 14.78163902 , 14.30584725 , 14.03682291
   ,14.79565262],[ 10.19202327,  10.89086707,  13.95090611,  15.43863452,  15.00457747
   ,12.10217006,  11.62925677,  13.07363615 , 14.38554367 , 16.77183782
   ,14.62290305,  15.65847177,  13.90414549 , 13.06784425 , 14.05108029
   ,12.03855953,  12.39813106,  12.17104967 , 12.54527139 , 12.13407995
   ,11.60882507,  12.15181197,  12.13755764 , 11.62853249 , 11.48114423
   ,11.54625161],
 [  6.24431741 , 12.30858036 , 13.96814986,  16.25425008 , 16.12335185
   ,12.26966821 , 12.53509476 , 12.62897807,  14.23015104 , 16.79148168
   ,15.6265662  , 15.01402939 , 13.83161194,  12.9756673  , 13.95998311
   ,12.1568191  , 12.90345332 , 12.47478498,  12.12890672 , 12.94906587
   ,11.8353989  , 11.88514701 , 11.88699365,  11.52119993 , 11.27416934
   ,11.67647737],[ 12.31976064,  13.73412266 , 14.19329312 , 16.04790164,  15.8723589
   ,12.94221262,  13.03257656,  12.48979591,  13.90527447 , 16.01766971
   ,15.43238328,  13.95412423,  12.65160944,  13.70066295 , 14.19794931
   ,11.70101531,  11.79956753,  11.96635649,  12.60966254 , 12.868622
   ,11.9675275 ,  12.46499711,  12.18174261,  11.67325929 , 11.57500619
   ,11.82410475],
 [ 10.74886098,  11.55737034 , 14.57792192 , 16.60121392 , 16.42162044
   ,13.27271026,  12.67131178,  12.95539067,  14.13900878,  16.46990646
   ,16.25665026,  14.84520322,  13.53791355,  12.30461423,  12.56090615
   ,11.38366537,  11.98616761,  11.63344379,  12.31683497,  13.03681372
   ,12.01509329,  12.41301889,  12.26167035,  11.91285738,  11.79984588
   ,11.99938285],[ 10.03915791,  11.18328542 , 14.14839179 , 15.8949371,   15.63383744
   ,11.41733333 , 12.35332274 , 12.1624037 ,  13.78157087,  16.31504377
   ,15.85090102 , 14.69370249 , 13.5598769 ,  12.5369398 ,  12.64320281
   ,10.92557275 , 11.04829281 , 10.89973832,  11.37623753,  11.46995361
   ,11.32229746 , 11.79886829 , 11.82724487,  11.40350474,  11.27130131
   ,11.64903198],
 [ 10.45053869 , 12.81332367 , 13.37561234,  16.25934518,  16.2525124
   ,13.68030032 , 12.93084441 , 12.79967863,  14.67939727,  16.60488373
   ,16.11729096 , 15.4109247  , 14.35024421,  13.23868447,  13.24612361
   ,11.88170165 , 11.63288343 , 11.46821363,  11.54154898,  11.60443436
   ,11.63838581 , 12.05370761 , 11.62771108,  11.33915496,  11.38731942
   ,11.68245347],[ 13.13488267,  13.23238182 , 14.07869644 , 16.13367109,  15.83168223
   ,13.22619693 , 12.89719339 , 12.65439005 , 14.29711579,  16.41927349
   ,15.39577371 , 14.75285355 , 14.47307961 , 13.29618906,  14.35532344
   ,12.26627549 , 11.86547578 , 12.60750139 , 12.25912267,  12.32265775
   ,11.74123634 , 12.30599297 , 12.34748213 , 12.04047865,  12.04506014
   ,12.40443355],
 [  7.49573273 , 12.35490846,  14.43890284,  16.84740495,  16.76793424,
   12.89415908 , 12.88426056,  12.39381975,  14.43010687,  17.20176489,
   16.21208384 , 15.15535951,  14.49905149,  13.11396329,  14.52135588,
   12.32212394 , 11.94564546,  12.86523727,  12.31949999,  13.23328817,
   12.01053848 , 12.46827629,  12.69416637,  12.08112189,  11.67045303,
   12.21009713],[  8.85818052,  13.12937216,  15.05178547,  15.79603937,  15.20451038
   ,13.18079006 , 13.00250113 , 13.58863272,  13.3092413 ,  14.78716276
   ,18.52875162 , 16.50842792 , 15.19011713,  15.18997564,  16.08854615
   ,14.90604472 , 13.53862383 , 12.33567135,  12.90375702,  13.45154039
   ,13.36299705 , 13.84992413 , 13.85577843,  13.55145392,  13.37362413
   ,13.72219369],
 [  6.65286314 , 12.95790645  ,14.09504591 , 14.76139765 , 14.5892875
   ,12.28254967 , 12.09819157 , 12.18319034,  13.2458002 ,  14.47786515
   ,15.78533567 , 14.30604933 , 13.24377865,  13.21842991,  14.82263452
   ,14.37739041 , 13.54954788 , 13.06154751,  12.58814562,  13.01683914
   ,13.55581472 , 13.98204437 , 13.87966062,  13.63230792,  13.47454174
   ,13.66511777],[ 11.11304572 , 13.06166248,  13.92369578 , 16.55354613,  15.18020711
   ,13.98466796,  13.31390424 , 13.28631957 , 13.93062047 , 16.03169137
   ,15.54451731,  14.84519742 , 13.38009131 , 13.99202769 , 14.54343011
   ,12.41036409,  12.26971292 , 11.99858743 , 11.86736957 , 12.7385077
   ,12.72417432,  13.28963204 , 13.3119539  , 13.11420646  ,12.96053703
   ,13.20922985],
 [ 12.68579393 , 11.77173513 , 13.883245    ,16.2523163  , 15.64759754
   ,13.73376089 , 12.94997321,  13.12281724 , 14.02274552,  16.1889957
   ,15.40022862 , 13.95278209,  12.95166534 , 13.51227643,  14.50419432
   ,12.09090213 , 12.41669541,  11.65755195 , 11.94623623,  12.73060982
   ,12.86999786 , 13.41645096,  13.20028734 , 12.92598043,  12.96347105
   ,13.22458554] ,[  6.17966803 , 11.99169909,  13.98815156,  15.66515993,  15.54742294
   ,13.07300135 , 12.76501245  ,14.04327697  ,16.63504911  ,17.15737078
   ,14.50491092  ,14.46394821  ,14.14880072  ,16.13922604  ,15.52612843
   ,11.56110095  ,13.60387481  ,14.02851925  ,13.61268962  ,13.66024839
   ,11.95218669  ,12.12421167  ,11.93516976  ,12.23148714  ,12.02856889
   ,12.56448646],
 [  5.21488405 , 12.0348342  , 13.69045008 , 16.44011722,  16.42758135
   ,13.74764801 , 12.74578942 , 14.38547835 , 16.74800907,  17.69036441
   ,15.39261193 , 15.26412947 , 14.90676395 , 15.86682611,  15.81085375
   ,13.01642742 , 13.71290019 , 13.67126757 , 13.36857246,  13.75910265
   ,12.00201517 , 11.48494334 , 11.54283796 , 11.73382755,  12.35121781
   ,12.70334193]        
           


           
           ]