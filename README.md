# English-exercises-AQA
Tests for [English-exercises](https://github.com/Areso/English-exercises)
> [!div class="nextstepaction"]
> [Learn about adding code to articles](code-in-docs.md)

While this for simple run, later I'll correct it.

```git clone https://github.com/lambotik/English-exercises-AQA.git```

```cd English-exercises-AQA```
 
```pip3 install -r requirements.txt```

```pytest -s -vv --alluredir=test_result/ tests/```
 
```allure serve test_result```
