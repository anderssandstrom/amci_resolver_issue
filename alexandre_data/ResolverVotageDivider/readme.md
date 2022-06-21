# Plot raw data

```
cat ResolverVotageDivider.csv  | grep "^13290776" | tr ";" " " | awk '{print $4}' | python ~/sources/ecmccomgui/pyDataManip/plotData.py ```

error:
cat ResolverVotageDivider.csv  | grep "^13290776" | tr ";" " " | awk '{print $2-$4}' | tee error_pos.log 

X-axis:
cat ResolverVotageDivider.csv  | grep "^13290776" | tr ";" " " | awk '{print $2}' | tee pos.log 

plot error vs pos:

python ~/sources/ecmccomgui/pyDataManip/plotDataXY.py pos.log error_pos.log
