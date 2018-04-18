## Data format ##
The CSV file with raw data is separated into columns of events and rows of people. Each person is identified by an ID number. Each event is labeled "Event i" where i is the column number. The availability is coded as follows:
* 1: Available from 8:30 to 9:00
* 2: Available from 9:00 to 9:30
* 3: Available from 9:30 to 10:00
* 4: Available from 10:00 to 10:30
* 5: Available from 10:30 to 11:00
* 6: Available from 11:00 to 11:30
* 0: Not available

Availability can be combined, but only in consecutive half hour blocks. For example, if someone is available from 9:00 to 10:30, the values will be (2 3 4). However, something like (1 3 4) will never appear because there is a gap in the middle. Also, no cell with a 0 will ever have any other values. This is so we don't have to worry about data validation.