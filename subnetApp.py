#!/usr/bin/python

import sys
import random

def split_fun(IP_address):
	"""This function takes an ip address like 1.1.1.1 and returns list of octacte 
		like 1.1.1.1 => ['1','1','1','1']"""
	#print "split_fun"
	IP_splt=[]
	IP_splt=IP_address.split('.')
	#print IP_splt
	return IP_splt


def IP_check(IP_address):
	"""Function takes IP address as input and returns 
		1 if IP is valid
		0 if IP is Invalid"""

	addr=[]
	addr=split_fun(IP_address)
	#print 'back to ip_check'
	if (len(addr)==4) and (1<=int(addr[0])<=223 and 0<=int(addr[1])<=225 and 0<=int(addr[2])<=225 and 0<=int(addr[3])<=225) and (int(addr[0])!=169 or int(addr[1])!=254) and (int(addr[0])!=127):
		return 1
	else:
		return 0

def subnet_check(subnet_mask):
	"""Function takes subnet mask as input and return
		1 if subnet valid
		0 if subnet invalid"""
	sub=[]
	sub=split_fun(subnet_mask)
	mask=[0,128,192,224,240,248,252,254,255]
	if (len(sub)==4) and (int(sub[0]) in mask and int(sub[1]) in mask and int(sub[2]) in mask and int(sub[3]) in mask) and (int(sub[0])>=int(sub[1])>=int(sub[2])>=int(sub[3])):
		return 1
	else:
		return 0

def ip_binary_list_fun(ip_address):
	"""Function takes an address as input and returns a list
		containing binary octates
		1.1.1.1 => ['00000001','00000001','00000001','00000001]"""
	ip_binary_list=[]
	ip_split=split_fun(ip_address)
	for oct in ip_split:
		bin_ip=bin(int(oct)).split('b')[1]
		if len(bin_ip)==8:
			ip_binary_list.append(bin_ip)
		elif len(bin_ip)<8:
			new_bin_ip=bin_ip.zfill(8)
			ip_binary_list.append(new_bin_ip)
	return ip_binary_list

def random_gen_fun(IP_addr,brd_mask):
	"""This function takes IP address and broadcast address as arguments
		and prints the IP address which will be randomly generated"""
	IP_list=split_fun(IP_addr)
	brd_list=split_fun(brd_mask)

	#print IP_list,brd_list

	new_IP=[]
	for i,oct_IP in enumerate(IP_list):
		#print i,oct_IP
		for j,oct_brd in enumerate(brd_list):
			#print j,oct_brd
			if i==j:
				#print 'i=j'
				if oct_IP==oct_brd:
					#print 'oct_IP=oct_brd'
					new_IP.append(oct_IP)
				else:
					#print 'oct_IP!=oct_brd'
					new_IP.append(str(random.randint(int(oct_IP)+1,int(oct_brd)-1)))

	final_random_ip='.'.join(new_IP)
	print 'Generated ip is:',final_random_ip,'\n'


def subnet_calc():
	"""Function takes no arguments and returns net_address, broadcast_address....etc"""
	try:
		print '\n'
		#chek IP is valid if not ask to re-enter it
		while True:
			IP_address=raw_input("Enter IP address:")
			ip_ok=IP_check(IP_address)
			
			#in_ok return 1 if ip address is valid
			if ip_ok:
				print "IP address is ok\n"
				break
			else:
				print "Invalid IP\n"
				continue
		#check subnet is valid, if not ask to reenter it
		while True:
			subnet_mask=raw_input("Enter subnet mask:")
			subnet_ok=subnet_check(subnet_mask)
			if subnet_ok:
				print "subnet ok\n"
				break
			else:
				print "Invalid subnet\n"
				continue
		
		#print "IP",IP_address,"is ok"
		#print "subnet",subnet_mask,"is ok"
		subnet_binary=ip_binary_list_fun(subnet_mask)
				
		#print subnet_binary
		joint_bin_sub=''.join(subnet_binary)
		#print joint_bin_sub
		#to count number of hosts, we count number of zeros in subnet 
		count_zeros=joint_bin_sub.count("0")
		count_ones=32-count_zeros
		number_of_hosts=abs(2**count_zeros-2)
		print 'number_of_hosts is:',number_of_hosts

		#to calculate network address and broadcast address
		ip_binary=ip_binary_list_fun(IP_address)
		joint_bin_ip=''.join(ip_binary)
		#print joint_bin_ip
		#this is for network address
		network_id_bin=joint_bin_ip[:count_ones]+'0'*count_zeros
		#print 'net id binary:',network_id_bin

		network_id_bin_list=[]
		for oct in range(0,len(network_id_bin),8):
			generated_oct=network_id_bin[oct:oct+8]
			network_id_bin_list.append(generated_oct)
		#print network_id_bin_list

		network_id_decimal=[]
		for each_oct in network_id_bin_list:
			network_id_decimal.append(str(int(each_oct,2)))
		print 'Network id is:','.'.join(network_id_decimal)

		#for broadcast id
		broadcast_id_bin=joint_bin_ip[:count_ones]+'1'*count_zeros
		#print 'broadcast id binary:',broadcast_id_bin,'\n'

		broadcast_id_bin_list=[]
		for oct in range(0,len(broadcast_id_bin),8):
			generated_oct=broadcast_id_bin[oct:oct+8]
			broadcast_id_bin_list.append(generated_oct)
		#print broadcast_id_bin_list

		broadcast_id_decimal=[]
		for each_oct in broadcast_id_bin_list:
			broadcast_id_decimal.append(str(int(each_oct,2)))
		
		b_cast='.'.join(broadcast_id_decimal)
		print 'broadcast id is:',b_cast,'\n'
		#print b_cast, 'is the b_cast'

		#random Ip generate function
		while True:

			generate=raw_input("Do u wanna generate an IP address??[y/n]:")

			if generate=='y':
				random_gen_fun(IP_address,b_cast)
				continue
			else:
				print "programe is halting...!!!!",'\n'
				break


	except:
		print "there is an exception"


def main():
	subnet_calc()

if __name__=='__main__':
	main()
