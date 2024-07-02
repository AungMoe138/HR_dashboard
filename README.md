## Lotteria Myanamr HR dashbord

# Description
Freelance project for Lotteria Myanmar's HR department.</br>
Lotteria is a Fastfood chain from South Korea.</br>
Lotteria Myanmar has over 50 fastfood stores opened under the management of MYCO co.ltd across Myanmar.</br>
In order to ensure smooth operations of all the branches, HR department is responsible for recruiting new employees and maintain the efficient menpower.</br>
Although the HR department is doing their best in recruting new employees, there were complaints that the stores were having difficulties in running operations due to lack of menpower.</br>

# Problem
There are several problems that the HR department is currently facing.
  1. Some branch managers are complaining that the HR department cannot provide enough menpower to their stores.
  2. HR team is having hard time maintaining useful database of recruitment and resignation of employee. Recruitment data is handle mainly by HR department but when the employee resign, the store manager is to keep track of the data.
  3. Without clear data insights, the HR department cannot make effective decitions in employee retaintion.


# Goal
My job as an Data Analyst is to:
  1. Create a consistant database and data model to allow HR department to track the employee turn over.
  2. Create a dashboard to visualize the related data to gain insight of the current menpower situation across all the branchs.
  3. Make recommendations for better data practices.
  4. Training the related personals for using and maintaining the dashboard.

# Solution
**Step 1.**</br>
The original recruitment data provided by HR department is in word document and there were hundreds of pages of data. It will consume a lot of time to copy the data and move them to the workable excel format.
Therefore, I worte a [python code](Extract_data_from_doc.py) to automate the process. Using panda libary, the pythone code will iteriate each pages to identify the data tables and copy the data into excel sheet.

**Step 2.**</br>
The employee resign data is in excel format but the data are not organized and there are also many unnecessary data spread out into huntreds of different sheets.
In order to extract only the necessary data all at once, I wrote the [python code](Excel_sheets_combine.py). The code will automatically extract specific columns and combined them into single excel sheet.

**Step 3.**</br>
After getting 2 output excel, I cleaned up the data from the excel file which include null or incorrect data types, make sure format are correct and there is no discrepancy.

**Step 4.**</br>
Input the excels sheets into Microsoft Power Bi and construct the data model to connect the two datasets.

![Sample Data Model](Data_model.png)




**Step 5.**
Create data visualization in Power Bi by creating Monthly recruitment/resignation data charts, top branchs with highest resignations, highest resigned positions and total turn over rate. 


![HR Dashboard](Dashboard.png)

# Summary
In the dashboard we can see the total employee recruitment and resignation, which can be filtered by branch and month.
The highest resignation happen in March and we can ovserved that the HR department had also done significant recruitment to compensate the turnover. However, the resign rate remained high in comparison to the recuritment rate.
We can see the top 3 position with highest trun over rate across most branches are Mate -1, Mate -2 and Mate -3 positions.
We can also see the top 5 branches, HTY, CT, JC, OSGC, O.MDY, WZYD with highest resignation.
The data set also have inconsistancy since the recruitment data only have until May and the resignation in July seem incomplete.

# Recommendation
1. The HR department should work closely with operations, especially in top 5 branches to identify the cause of high turn over.
2. Investigate furthur to the resign data in March to identify the cause of spike. This can be useful insight for referenceing in the future.
3. Have constructive conversation with employees, especially the positions with highest resignation, in order to find out the reasons and difficuilts at work causing to resign.
4. Create a centralized database to easy track the employee data. It is recommended to build the automated system to avoid the human errors.
5. Regular training sessions to the HR department members for the better data practics.


