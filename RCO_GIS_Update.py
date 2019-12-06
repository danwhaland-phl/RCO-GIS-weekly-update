# Import modules
import arcpy

# import smtplib for emails
import smtplib

# import os for environment variables
import os

# email variables
sender = os.environ.get('DPDAppsProd_Email')
receivers = [os.environ.get('Pauline_Email'), os.environ.get('Dan_Email')]
password = os.environ.get('DPDAppsProd_password') 

message = """Subject: RCO Ready for Upload

The RCO GIS layer has been updated and is ready for an upload. Thanks!

-DPD Apps Prod-bot
"""

smtpObj = smtplib.SMTP(host='smtp.office365.com', port=587)
smtpObj.starttls()
smtpObj.login(sender,password)

# Set workspace
arcpy.env.workspace = "P:/Zoning/RCO/RCO Data Entry/Zoning_RCO.gdb"

# Allow overwrite of existing files
arcpy.env.overwriteOutput = True

# Since arcpy.env.overwriteOutput does not seem to be working in ArcPro 2.4, use this line to delete the Zoning_RCO_rev field before creating it again through arcpy.CopyFeatures
if arcpy.Exists("Zoning_RCO_rev"):
    arcpy.Delete_management("Zoning_RCO_rev")

# Create variables
CurrRCO = "Zoning_RCO"
NewRCO = "Zoning_RCO_rev"

# Copy Zoning_RCO to Zoning_RCO_New.gdb as Zoning_RCO_rev
arcpy.CopyFeatures_management(CurrRCO, NewRCO)

# Change field names to match OpenMaps schema
arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Organization_N", "Organization_Name")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Organization_A", "Organization_Address")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Meeting_Locati", "Meeting_Location_Address")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Org_Type", "Org_Type")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Preffered_Cont", "Preffered_Contact_Method")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Primary_Name", "Primary_Name")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Primary_Addres", "Primary_Address")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Primary_Email", "Primary_Email")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Primary_Phone", "Primary_Phone")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_P_Phone_Ext", "P_Phone_Ext")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Alternate_Name", "Alternate_Name")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Alternate_Addr", "Alternate_Address")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Alternate_Emai", "Alternate_Email")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Alternate_Phon", "Alternate_Phone")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_A_Phone_Ext", "A_Phone_Ext")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_ExpirationYear", "ExpirationYear")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Effective_Date", "Effective_Date")

arcpy.AlterField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_LNI_ID", "LNI_ID")

# Delete extra fields
arcpy.DeleteField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Folder_Locatio")

arcpy.DeleteField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Application_Da")

arcpy.DeleteField_management(NewRCO, "Zoning_RCO_Org_Name")

arcpy.DeleteField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Ward_Number")

arcpy.DeleteField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Ward_Political")

arcpy.DeleteField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Status")

arcpy.DeleteField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Docs_Recieved")

arcpy.DeleteField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Council_Distri")

arcpy.DeleteField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_Notes")

arcpy.DeleteField_management(NewRCO, "RCO_Registration_dbo_RCO_Registration_Information_ESRI_OID")

# send the email 
smtpObj.sendmail(sender, receivers, message)
smtpObj.quit()