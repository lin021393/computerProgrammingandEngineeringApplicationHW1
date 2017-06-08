import re

def main():
	E=20000
	i=0
	xCoordOfPoints=[]	#	點的x座標
	yCoordOfPoints=[]	#	點的y座標
	numOfBars=0		#	bars的數量
	originOfBars=[]		#	每個bar的起點
	endOfBars=[]		#	每個bar的終點
	area=[]		#	紀錄每個area的面積。
	numOfAreas=0	#	紀錄有幾個面積。
	lengthsOfBars=[]		#	每個bar的長度

	file=open('0551284IN.txt','r')	# 開檔讀檔

	while True:		#	切割字串
		line = file.readline()
		elements=re.split(r'[;,=\s]\s*', line)
		if not line: break
		if i==0:
			numOfPoints=float(elements[1]);
		elif i>=1 and i<=numOfPoints:
			xCoordOfPoints.append(float(elements[1]))
			yCoordOfPoints.append(float(elements[2]))
		elif i==numOfPoints+1:
			numOfBars=int(elements[1], 10);
		elif i>=numOfPoints+2 and i<=numOfPoints+numOfBars+1:
			originOfBars.append(int(elements[1], 10))
			endOfBars.append(int(elements[2], 10))
		else:
			area.append(float(elements[1]))
			numOfAreas +=1
		i +=1

	j=0
	while j<=numOfBars-1:	#	計算每條bar的長度，用((x1-x2)^2+(y1-y2)^2)^0.5的坐標軸距離公式求出bar的長度。
		lengthsOfBars.append(((xCoordOfPoints[originOfBars[j]-1]-xCoordOfPoints[endOfBars[j]-1])**2+(yCoordOfPoints[originOfBars[j]-1]-yCoordOfPoints[endOfBars[j]-1])**2)**0.5)
		j +=1

	FW = open('0551284OUT.txt','w')		#	開要寫入資料的檔案

	k=0
	while k<=numOfAreas-1:	#	寫入每條bar的長度資料與E * A / L資料到0551284OUT.txt中。
		FW.write('length of bar'+str(k+1)+': '+str(lengthsOfBars[k])+',  E * A / L: '+str(E*area[k]/lengthsOfBars[k])+'\n')
		k +=1

	FW.close()	#	關閉檔案。


if __name__ == '__main__':
	main()