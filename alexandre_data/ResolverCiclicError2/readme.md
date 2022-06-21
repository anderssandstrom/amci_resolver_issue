# Plot raw data

```
cat ResolverCiclicError2.csv | grep "^13290008" | tr ";" " " | awk '{print $4}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py 
```

dataset1: 1700..2700
dataset2: 3250..4250


cat ResolverCiclicError2.csv | head -n 2750 | tail -n 1050 | tee dataset_1.log
cat ResolverCiclicError2.csv | head -n 4300 | tail -n 1050 | tee dataset_2.log

## Rawdata plot
cat dataset_*.log | grep "^13290008" | tr ";" " " | awk '{print $4}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py 

## Error


```
cat ResolverCiclicError2.csv  | grep "^13290008" | tr ";" " " | awk '{print $4}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py 
```

error:
cat ResolverCiclicError2.csv  | grep "^13290008" | tr ";" " " | awk '{print $2-$4}' | tee error_pos.log 

X-axis:
cat ResolverCiclicError2.csv  | grep "^13290008" | tr ";" " " | awk '{print $2}' | tee pos.log 

plot error vs pos:

python ~/sources/ecmccomgui/pyDataManip/plotDataXY.py pos.log error_pos.log
