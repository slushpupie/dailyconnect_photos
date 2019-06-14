# DailyConnect Photo Downloader

This python3 script will download photos from DailyConnect.com.  To use this script, 
set the following environment variables:

 * `DC_EMAIL`: Your login to DailyConnect
 * `DC_PASS`: Your password to DailyConnect
 * `DC_STARTDATE`: The first date to gather photos (YYMMDD format)
 * `DC_ENDDATE`: The last date to gather photos (YYMMDD format)

It will download the photos into a folder named after the kid ID in DailyConnect, and the photo caption will be placed in a text file next to it.  
