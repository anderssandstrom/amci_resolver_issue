# Plot raw data

```
cat VoltageDividerSineCosCoils.csv  | grep "^1329079" | tr ";" " " | awk '{print $4}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py 
```

error:
```
cat VoltageDividerSineCosCoils.csv  | grep "^1329079" | tr ";" " " | awk '{print $4-$2}' | tee error_pos.log 
```

X-axis:
```
cat VoltageDividerSineCosCoils.csv  | grep "^1329079" | tr ";" " " | awk '{print $2}' | tee pos.log 
```
plot error vs pos:
```
python ~/sources/ecmccomgui/pyDataManip/plotDataXY.py pos.log error_pos.log
```

# New style
```
Forward 0..1500   (head -n 1500)
Backward 1500..3000 (tail -n 1500)

Add dummy timestamp "MCAG:TS-EVR-01:1hzCnt-I        2022-06-01 11:33:06.999999 275
```

## Forward Y
```
cat VoltageDividerSineCosCoils.csv  | head -n 1500 | grep "^1329079" | tr ";" " " | awk '{print "ForwardY 2022-06-01 11:33:06.999999 " $4-$2}' | tee error_pos_fwd.log 
```
## Forward X
```
cat VoltageDividerSineCosCoils.csv  | head -n 1500 | grep "^1329079" | tr ";" " " | awk '{print "ForwardX 2022-06-01 11:33:06.999999 " $2}' | tee pos_fwd.log 
```

## Backward Y
```
cat VoltageDividerSineCosCoils.csv  | tail -n 1500 | grep "^1329079" | tr ";" " " | awk '{print "BackwardY 2022-06-01 11:33:06.999999 " $4-$2}' | tee error_pos_bwd.log 
```

## Backward X
```
cat VoltageDividerSineCosCoils.csv  | tail -n 1500 | grep "^1329079" | tr ";" " " | awk '{print "BackwardX 2022-06-01 11:33:06.999999 " $2}' | tee pos_bwd.log 
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
cat VoltageDividerSineCosCoils.csv  | grep "^1329079" | tr ";" " " | awk '{print $4-$2}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py
Samples[3005] -3.26582..2.74551, mean: -0.2726622049364392, std: 1.3667302359738325
```
## Best case
```
cat VoltageDividerSineCosCoils.csv  | grep "^1329079" | tr ";" " " | awk '{print $4-$2+3.26582-6.01133/2}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py
Samples[3005] -3.00567..3.00566, mean: -0.012507241645923466, std: 1.3667300879884554
```

## Worst case
```
cat VoltageDividerSineCosCoils.csv  | grep "^1329079" | tr ";" " " | awk '{print $4-$2+3.26582}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py
Samples[3005] -3.02069e-06..6.01133, mean: 2.993157793124563, std: 1.3667302090822049
```
