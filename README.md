## Lotteria Myanamr HR dashboard

# Description
Freelance project for Lotteria Myanmar's HR department. </br>
Lotteria is a Fast-food chain from South Korea. </br>
Lotteria Myanmar has over 50 fast food stores opened under the management of MYCO Co.ltd across Myanmar. </br>
In order to ensure smooth operations of all the branches, HR department is responsible for recruiting new employees and maintain the efficient manpower.</br>
Although the HR department is doing their best in recruiting new employees, there were complaints that the stores were having difficulties in running operations due to lack of manpower.</br>

# Problem
There are several problems that the HR department is currently facing.
  1. Some branch managers are complaining that the HR department cannot provide enough manpower to their stores.
  2. The HR team is having a hard time maintaining a useful database of recruitment and resignation of employee. Recruitment data is handled mainly by the HR department but when the employee resigns, the store manager is to keep track of the data.
  3. Without clear data insights, the HR department cannot make effective decisions in employee retention.


# Goal
My job as an Data Analyst is to:
  1. Create a consistent database and data model to allow the HR department to track the employee turnover.
  2. Create a dashboard to visualize the related data to gain insight of the current manpower situation across all the branches.
  3. Make recommendations for better data practices.
  4. Training the related personals for using and maintaining the dashboard.

# Solution
**Step 1.**

The original recruitment data provided by the HR department is in word document and there were hundreds of pages of data. It will take a lot of time to copy the data and move them to the workable excel format.
Therefore, I wrote a [python code](Extract_data_from_doc.py) to automate the process. Using panda library, the python code will iterate each page to identify the data tables and copy the data into excel sheet.

**Step 2.**

The employee resign data is in excel format, but the data is not organized and there are also many unnecessary data spread out into hundreds of different sheets.
In order to extract only the necessary data all at once, I wrote the [python code](Excel_sheets_combine.py). The code will automatically extract specific columns and combine them into single excel sheet.

**Step 3.**

After getting 2 output excels, I cleaned up the data from the excel file which include null or incorrect data types, make sure format are correct and there is no discrepancy.

**Step 4.**

Input the excels sheets into Microsoft Power Bi and construct the data model to connect the two datasets.

![Sample Data Model](Data_model.png)




**Step 5.**

Create data visualization in Power Bi by creating Monthly recruitment/resignation data charts, top brands with highest resignations, highest resigned positions and total turnover rate. 


![HR Dashboard](Dashboard.png)

# Summary
In the dashboard we can see the total employee recruitment and resignation, which can be filtered by branch and month.</br>
The highest resignation happened in March, and we can observe that the HR department had also done significant recruitment to compensate the turnover. However, the resign rate remained high in comparison to the recruitment rate.</br>
We can see the top 3 position with highest turnover rate across most branches are Mate -1, Mate -2 and Mate -3 positions.</br>
We can also see the top 5 branches, HTY, CT, JC, OSGD, O.MDY, WZYD with highest resignation.</br>
The data set also have inconsistency since the recruitment data only have until May and the resignation in July seem incomplete.</br>

# Recommendation
1. The HR department should work closely with operations, especially in top 5 branches to identify the cause of high turnover.
2. Investigate further to the resign data in March to identify the cause of spike. This can be useful insight for referencing in the future.
3. Have constructive conversation with employees, especially the positions with highest resignation, to find out the reasons and difficulties at work causing them to resign.
4. Create a centralized database to easily track the employee data. It is recommended to build an automated system to avoid the human errors.
5. Regular training sessions for the HR department members for better data practices.


