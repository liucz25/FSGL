g++ -fPIC -shared test.cpp -o libtest_1.so

g++ -fPIC -shared test.cpp -o libtest_2.so

g++ -g -Wl,--no-as-needed -ldl main.cpp -rdynamic
