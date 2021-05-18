tensorflow version 1.x, 

결과 평가를 위한 fid score 도출 오픈소스
ver1 : https://machinelearningmastery.com/how-to-implement-the-frechet-inception-distance-fid-from-scratch/

ver2 : 

![1_tJmwViZesuFM89TcVN7J3A](https://user-images.githubusercontent.com/68414594/117540393-2c2ac100-b04a-11eb-81b5-fb2e626fa04b.png)

autoencoder로 생성한 영상 (g)과 기본 사진(x)의 특징 벡터값의 차이의 제곱 및 두 벡터의 공분산을 계산한 값을 fid score라고 할 수 있으며,
이를 계산하여 결과를 도출한다.

단, 해당 코드는 GAN의 결과물의 fid score를 도출해 내는 것에 초점을 두었기 때문에 autoencoder에 맞춰 fid score을 낼 수 있도록 수정하여 사용했다.
