# RSA

## 使い方

create_ned.shを実行した後、

RSA.shを実行してください。

## create_ned.sh

ned.pyを実行します。

## ned.py

pqe.txt　から　ned.txt (秘密鍵と公開鍵)を作成します。

## RSA.sh

rsa.pyを実行します。

## rsa.py

ned.txt　を用いて、暗号化・複合化します。

eかd　を入力した後、nより小さな数字を入力してください。

## pqe.txt

上から順にp,q,eです。

p,q：異なる素数(大きいほど強度が増します。)

e：(p-1)(q-1)と互いに素な数字

デフォルトは、

999999999999989

10000000000004369

65537

です。

## ned.txt

create.shを実行すると作成されます。

上から順にn,e,dです。

n：p*q

e：pqe.txtと同じもの(公開鍵)

d：秘密鍵
