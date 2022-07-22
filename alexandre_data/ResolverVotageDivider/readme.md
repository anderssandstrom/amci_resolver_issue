# Plot raw data

```
cat ResolverVotageDivider.csv  | grep "^13290776" | tr ";" " " | awk '{print $4}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py
```

error:
```
cat ResolverVotageDivider.csv  | grep "^13290776" | tr ";" " " | awk '{print $4-$2}' | tee error_pos.log 
```

X-axis:
```
cat ResolverVotageDivider.csv  | grep "^13290776" | tr ";" " " | awk '{print $2}' | tee pos.log 
```

plot error vs pos:
```
python ~/sources/ecmccomgui/pyDataManip/plotDataXY.py pos.log error_pos.log
```

# New style
```
Forward 0..2500   (head -n 2500)
Backward 2500..3935 (tail -n 1435)

Add dummt timestamp "MCAG:TS-EVR-01:1hzCnt-I        2022-06-01 11:33:06.999999 275
```

## Forward Y
```
cat ResolverVotageDivider.csv  | head -n 2500 | grep "^13290776" | tr ";" " " | awk '{print "ForwardY 2022-06-01 11:33:06.999999 " $4-$2}' | tee error_pos_fwd.log 
```

## Forward X
```
cat ResolverVotageDivider.csv  | head -n 2500 | grep "^13290776" | tr ";" " " | awk '{print "ForwardX 2022-06-01 11:33:06.999999 " $2}' | tee pos_fwd.log 
```

## Backward Y
```
cat ResolverVotageDivider.csv  | tail -n 1435 | grep "^13290776" | tr ";" " " | awk '{print "BackwardY 2022-06-01 11:33:06.999999 " $4-$2}' | tee error_pos_bwd.log 
```

## Backward X
```
cat ResolverVotageDivider.csv  | tail -n 1435 | grep "^13290776" | tr ";" " " | awk '{print "BackwardX 2022-06-01 11:33:06.999999 " $2}' | tee pos_bwd.log 
```

## plot
```
cat error_pos_fwd.log pos_fwd.log error_pos_bwd.log pos_bwd.log | python ../../plotError.py
```
## Overview
```
python  ../../plotOverview.py pos.log resolver_pos.log 
```
# Statistics

## As recorded
```
cat ResolverVotageDivider.csv  | grep "^13290776" | tr ";" " " | awk '{print $4-$2}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py
Samples[3935] -2.47429..1.43504, mean: -0.41368160183979674, std: 0.9956647252974441
```
## Best case

```
cat ResolverVotageDivider.csv  | grep "^13290776" | tr ";" " " | awk '{print $4-$2+2.47429-3.90933/2}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py
Samples[3935] -1.95466..1.95466, mean: 0.10594337102922487, std: 0.9956647922140913
```
## Worst case
```
cat ResolverVotageDivider.csv  | grep "^13290776" | tr ";" " " | awk '{print $4-$2+2.47429}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py
[3935] 2.15542e-06..3.90933, mean: 2.060608385978506, std: 0.9956647347321389
```
