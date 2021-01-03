# -*- coding: utf-8 -*-
"""
Created on Wed Des  30 21:17:06 2020

@author: DIVYA
"""

import mysql.connector

con = mysql.connector.connect(host="localhost",username="root",passwd="Chhaya@60")

cursur = con.cursor()
cursur.execute("CREATE database IF NOT EXISTS movie")
cursur.execute("USE movie")

class seller:
	def setup():
		cursur.execute("CREATE TABLE IF NOT EXISTS seat (seat_row decimal NOT NULL PRIMARY KEY, vaccancy VARCHAR(150) NOT NULL)")
		cursur.execute("CREATE TABLE IF NOT EXISTS buyer_info (name VARCHAR(20) NOT NULL,phone VARCHAR(20) NOT NULL,age INT(2) NOT NULL,gender CHAR(1) NOT NULL,ticket_prize INT(2),seat_number VARCHAR(3) NOT NULL)")
		cursur.execute("DELETE FROM SEAT")
		cursur.execute("DELETE FROM buyer_info")
		print("Enter the number of rows:")
		row = int(input())
		print("Enter the number of seats in row:")
		col = int(input())
		s = []
		for i in range(col):
			s.append(0)
		#seat per row ....done
		for i in range(row):
			query = "INSERT INTO seat (seat_row,vaccancy) values ({},'{}')".format(i+1,s)
			cursur.execute(query)
		con.commit()
		print("Rows and coloumns creation successfull....")

	def show_seats():
		query = "select * from seat"
		cursur.execute(query)
		data = cursur.fetchall()
		d=eval(data[0][1])
		a = '  '
		for i in range(len(d)):
			a += ' '+ str(i+1)
		print(a)
		for i in data:
			s = ''
			for j in eval(i[1]):
				if j == 1:
					s += ' B'
				elif j == 0:
					s += ' S'
			print((data.index(i)+1),s)

	def statistics():
		query = "select vaccancy from seat"
		cursur.execute(query)
		data = cursur.fetchall()
		r_len = len(data)
		c_len = len(eval(data[0][0]))
		total_count = r_len * c_len
		total_income = 0
		if total_count > 60:
			z = (total_count//2)
			y = total_count-z
			total_income = (z*8) + (y*10)
		elif total_count <= 60:
			total_income = 600
		count = 0
		c_income = 0
		query1 = "select ticket_prize from buyer_info"
		cursur.execute(query1)
		data1 = cursur.fetchall()
		for i in data1:
			count += 1
			c_income += int(i[0])
		per = (count/total_count)*100
		print("Number of purchased tickets:",count)
		print("Percentage:", per)
		print("Current income:",c_income,"$")
		print("Total income:",total_income,"$")

		
	def booked_ticket_buyer_info():
		query = "select * from buyer_info"
		cursur.execute(query)
		data = cursur.fetchall()
		for i in data:
			print("==========***========")
			print("Name = ",i[0])
			print("Phone Number = ",i[1])
			print("Age = ",i[2])
			print("Gender = ",i[3])
			print("Ticket prize = ",i[4],"$")
			print("Seat number = ",i[5])
			print("==========***========")

	def all_ticket_buyer_info():
		query = "select * from all_buyer_info"
		cursur.execute(query)
		data = cursur.fetchall()
		for i in data:
			print("==========***========")
			print("Name = ",i[0])
			print("Phone Number = ",i[1])
			print("Age = ",i[2])
			print("Gender = ",i[3])
			print("Ticket prize = ",i[4],"$")
			print("Seat number = ",i[5])
			print("==========***========")

class buyer:

	def buy_ticket():
		# taking usser data
		print("type your name = ")
		name = str(input("name = "))
		print("type your phone number")
		phone = str(input("phone number = "))
		print("type your age")
		age = int(input("age = "))
		print("type your gender")
		gender = str(input("male or female type M/F/O= "))
		query = "select * from seat"
		cursur.execute(query)
		data = cursur.fetchall()
		print("select row")
		#taking user prefered row
		row = int(input())
		row_list = eval(data[row-1][1])
		ticket_prize = 10
		r_len = len(data)
		y = eval(data[1][1])
		c_len = len(y)
		seat_count = r_len * c_len
		# caluclating the prize of ticket asper rules
		if seat_count > 60 and row <= (len(data)/2):
			ticket_prize = 8
		while True:
			if 0 not in row_list:
				print('no vaccant seat in this row')
				row = int(input())
			elif 0 in row_list:
				print("select seat number")
				s = ''
				for i in row_list:
					if i == 1:
						s += ' B'
					elif i == 0:
						s+= ' S'
				print(s)
				break
				
		col = int(input())
		while True:
			if row_list[col-1] == 1:
				print('this seat is not vaccant')
				col = int(input())
			elif row_list[col-1] == 0:
				new = row_list
				new[col-1] = 1
				break
		# getting seat number according to row and coloumns
		seat_num = chr(96+row)+str(col)
		up_query = "UPDATE seat SET vaccancy = '{}' WHERE seat_row = {}".format(str(new),row)
		cursur.execute(up_query)
		data_query = "INSERT INTO buyer_info (name,phone,age,gender,ticket_prize,seat_number) VALUES ('{}','{}',{},'{}',{},'{}')".format(name,phone,age,gender,ticket_prize,seat_num)
		cursur.execute(data_query)
		con.commit()
		print('seat booking successfull, your ticket prize is',ticket_prize,"$",'and your seat number is',seat_num)
				

	def exit():
		cursur.execute("CREATE TABLE IF NOT EXISTS all_buyer_info (name VARCHAR(20),phone VARCHAR(20),age INT(2),gender CHAR(1),ticket_prize INT(2),seat_number VARCHAR(3) NOT NULL)")
		cursur.execute("INSERT INTO all_buyer_info (name,phone,age,gender,ticket_prize,seat_number) select * from buyer_info")
		con.commit()

