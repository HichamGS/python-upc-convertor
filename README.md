# Check Digit Calculator

This Universal Product Code Converter 

A Python Class to calculate check digit for 11 digit 
UPC's

NB , you'll need to install Pandas
```
python3 -m pip install pandas
```


you can either :

convert a single 11 digit upc

```
upc_s = rand_11_digits_upc()
obj = CheckDigitCalc()
print(obj.get_full_upc(upc_s))
```

or you can convert a upcs csv file

```
obj = ProcessCSVRawData()
obj.read_file_info('./', 'refs.csv');
obj.update_upc_df()
obj.write_upc_csv('./', 'refs-updated.csv')
 ```


Feel free to run the unit tests and improve them as well!