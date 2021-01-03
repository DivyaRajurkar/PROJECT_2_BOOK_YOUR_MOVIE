# -*- coding: utf-8 -*-
"""
Created on Wed Dec  30 20:15:36 2020

@author: DIVYA
"""

from theatre import buyer,seller




while True:
	print("press 1 to select new theatre layout")
	print("press 2 to book todays show tickets")
	print("press 3 to select all ticket buyer information list")
	print("press 4 to close this application")
	out = int(input())
	if out == 1:
		seller.setup()

	elif out == 2:
		x=0
		while x!=5 :
			print("==========***========")
			print("1. show seats")
			print("2. buy a ticket")
			print("3. statistics")
			print("4. show booked tickets user info")
			print("0. Exit")
			print("==========***========")
			i = int(input())
			if i == 1:
				seller.show_seats()
			elif i==2:
				buyer.buy_ticket()
			elif i==3:
				seller.statistics()
			elif i==4:
				seller.booked_ticket_buyer_info()
			if i==0:
				buyer.exit()
				x = 5

	elif out == 3:
		seller.all_ticket_buyer_info()

	elif out == 4:
		break

