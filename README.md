# VacciDate

Hope you guys are safe and healthy in this challenging time.
In this challenging time, if we want to stay one step ahead of the CoVID-19 virus, we need to get vaccinated as soon as we can.
### But what are the challenges?
Due to the shortage of Vaccine in India, it gets little difficult to get the slot booked.
Hospitals update the slot details as soon as they get new doses. And to book the slot, we need to either keep track of the time slots are updated, or keep refreshing CoWIN portal.

### Welcome to VacciDate Bot!!!
This bot will assist you in getting the slot booked.
A combination of Telegram Bot and algorithm in Python, VacciDate Bot notify you whenever the slot is available in your area.

There are different options avaialble in the BOT

## Search options
1. Search for slots based on District
2. Search for slots based on Pincode

## Age Group options
1. Search for slots for 18+
2. Search for slots for 45+
3. Search for slots for both 18+ and 45+

## Dose options
1. Search for only 1st Dose vaccine
2. Search for only 2nd Dose vaccine
3. Search for both 1st and 2nd Dose vaccine

## Prerequisite
1. Python3.6 and above is needed
2. Account in Telegram

## Setup
### Telegram BOT setup
To get detailed steps to setup your telegram bot please refer the blog:
<link to blog>
If you already know how to setup a Telegram BOT and Telegram Channel, please create these two things and keep BOT Token and Chat Id handy (we would need that as part of setup).

### Code base
Clone the repository on your local system or download and extract the zip file.

### Installation Steps
1. Open command promt or Terminal in your system.
2. Navigate to the folder where the codebase is present.
3. Create a new pipenv using below command:
```python
pipenv shell
```
4. If pipenv is not installed in your system, you can install it using below command:
```python
pip install pipenv
```
5. Install all the required dependencies using below command:
```python
pipenv install
```
6. Congratulations!!! Installation is compelte.

### Execute program
1. Before we execute the program, make sure the two required env variables are exported.
2. Open up "env" file and update Telegram Bot token in "telegram_bot_token" and Telegram channel Chat Id in "telegram_chat_id".
3. Run below command on your command promt/terminal:
```python
source ./env
```
4. You should get the correct values to Token and Chat Id when running below command:
```python
echo $telegram_bot_token
echo $telegram_chat_id
```
5. Now run below command to start the program:
```python
python main.py -d <district_id>
```
### Different paramteres available
There are 2 main mode in which this BOT works
#### District Mode: 
The availability of vaccination slots is checked for the whole district (need to provide district id corresponding to your district from the list available in "data/district_data").
#### Pincode Mode: 
Along with the district id provide the pincode of your area, and the BOT will filter the results for your specific area.

### Sub-parameters available
There are few more parameters using which the output result can be filtered
#### Age Group:
The age group can be selected when running the python script. "-a" or "--age_group" can be used to filter results for 18+ or 45+ vaccine slot.
##### Pass 18 if you only want to track for 18+ availability
##### Pass 45 if you only want to track for 45+ availability
##### Dont pass this parameter if you want to track both 18+ and 45+

#### Dose:
The number of dose can also be filtered. "-dose" can be used to filter results based on 1st Dose or 2nd Dose
##### Pass 1 if you only want to track 1st dose availability
##### Pass 2 if you only want to track 2nd dose availability
##### Dont pass this parameter if you want to track both 1st and 2nd dose availability

Execute below command for more details
```python
python3 main.py --help
```
