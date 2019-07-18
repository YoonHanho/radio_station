import pandas as pd
import numpy as np
import os

# 방송국 리스트 만들기
radio = [['일반', 'CBS음악FM', 'http://aac.cbs.co.kr/cbs939/cbs939.stream/playlist.m3u8'],
		['일반', 'CBS표준FM', 'http://aac.cbs.co.kr/cbs981/cbs981.stream/playlist.m3u8'],
		['일반', 'MBC원주표준FM', 'mms://live.wjmbc.co.kr/fm2 '], 
		['일반', 'MBC원주FM4U', 'mms://live.wjmbc.co.kr/fm989'], 
		['Jazz', 'DI Radio Digital Impulse', 'http://5.39.71.159:8950/stream'],
		['클래식', 'DI Radio Digital Impulse', 'http://5.39.71.159:8978/stream'] ,
		['클래식', 'Linn Classical', 'http://89.16.185.174:8004/stream'], 
		['클래식', 'Hi On Line Classic Radio', 'http://82.94.166.107:8088/'], 
		['클래식', 'Otto"s Classical Music', 'http://185.33.21.112:80/classical_128'], 
		['클래식', 'Positively Baroque EU', 'http://46.101.178.228:7002/320'], 
		['클래식', 'The Organ Experience EU', 'http://46.101.178.228:7006/320'], 
		['Easy Listening', 'America"s Best Ballads', 'http://185.33.21.112:80/onelive_128'], 
		['Blues', 'DI Radio Digital Impulse - Blues', 'http://5.39.71.159:8990/stream'],  
		['월드뮤직', 'Catolica Springfield 102.5', 'http://167.114.157.212:8324/stream'],  
		['Rock', 'Rock Melodic Radio', 'http://95.217.68.35:8124/stream']]

radio_stations = pd.DataFrame(radio, columns=['장르','방송국','URL'])

while True:
	try:
		# 방송국 리스트 출력 후 선택값 받기 
		print(radio_stations.iloc[:,:2])
		station_id = input("방송국 숫자를 입력하세요(나가기, 방송 중단은 Q) : ")		
		if station_id.upper() == 'Q':
			break

		# 선택한 방송국 재생
		play_code = 'mplayer ' + radio_stations.iloc[int(station_id), 2]
		print(play_code)
		print('-'*50)
		os.system(play_code)
		print("-"*50, "\n이용해주셔서 감사합니다. 방송을 끝냅니다")
		break
	except:
		pass







