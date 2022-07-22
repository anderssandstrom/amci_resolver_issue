# Plot raw data

```
cat ResolverCiclicError2.csv | grep "^13290008" | tr ";" " " | awk '{print $4}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py 
```

dataset1: 1700..2700
dataset2: 3250..4250

```
cat ResolverCiclicError2.csv | head -n 2750 | tail -n 1050 | tee dataset_1.log
cat ResolverCiclicError2.csv | head -n 4300 | tail -n 1050 | tee dataset_2.log
```

## Rawdata plot
```
cat dataset_*.log | grep "^13290008" | tr ";" " " | awk '{print $4}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py 
```
## Error

```
cat ResolverCiclicError2.csv  | grep "^13290008" | tr ";" " " | awk '{print $4}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py 
```

error:
```
cat ResolverCiclicError2.csv  | grep "^13290008" | tr ";" " " | awk '{print $4-$2}' | tee error_pos.log 
```

X-axis:
```
cat ResolverCiclicError2.csv  | grep "^13290008" | tr ";" " " | awk '{print $2}' | tee pos.log 
```
plot error vs pos:
```
python ~/sources/ecmccomgui/pyDataManip/plotDataXY.py pos.log error_pos.log
```

# New style
```
Forward 0..3000   (head -n 3000)
Backward 3001..4563 (tail -n 1563)

Add dummt timestamp "MCAG:TS-EVR-01:1hzCnt-I        2022-06-01 11:33:06.999999 275  "
```

## Forward Y
```
cat ResolverCiclicError2.csv  | head -n 3000 | grep "^13290008" | tr ";" " " | awk '{print "ForwardY 2022-06-01 11:33:06.999999 " $4-$2}' | tee error_pos_fwd.log 
```

## Forward X
```
cat ResolverCiclicError2.csv  | head -n 3000 | grep "^13290008" | tr ";" " " | awk '{print "ForwardX 2022-06-01 11:33:06.999999 " $2}' | tee pos_fwd.log 
```

## Backward Y
```
cat ResolverCiclicError2.csv  | tail -n 1563 | grep "^13290008" | tr ";" " " | awk '{print "BackwardY 2022-06-01 11:33:06.999999 " $4-$2}' | tee error_pos_bwd.log 
```

## Backward X
```
cat ResolverCiclicError2.csv  | tail -n 1563 | grep "^13290008" | tr ";" " " | awk '{print "BackwardX 2022-06-01 11:33:06.999999 " $2}' | tee pos_bwd.log 
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
cat ResolverCiclicError2.csv  | grep "^13290008" | tr ";" " " | awk '{print $4-$2}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py
Samples[4535] -15.0418..4.10925, mean: -2.667513986587255, std: 4.720417740329049
```

## Best case
```
cat ResolverCiclicError2.csv  | grep "^13290008" | tr ";" " " | awk '{print $4-$2+5.466275}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py 
Samples[4535] -9.57551..9.57552, mean: 2.7987609944432195, std: 4.7204179893924
```

## Worst case
```
cat ResolverCiclicError2.csv  | grep "^13290008" | tr ";" " " | awk '{print $4-$2+15.0418}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py
Samples[4535] 1.61336e-05..19.151, mean: 12.374285939674444, std: 4.7204179040554335
```
