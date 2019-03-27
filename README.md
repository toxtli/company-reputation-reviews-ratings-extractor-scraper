# Reviews extractor

## Instructions

These are command line parameters supported:

```
usage: app.py [-h] [--site SITE] [--ratings RATINGS] [--companies COMPANIES]

This script extract reviews deom companies.

optional arguments:
  -h, --help            show this help message and exit
  --site SITE           The website from where the reviews are extracted. The valid options are sitejabber and consumeraffairs
  --ratings RATINGS     The ratings to extract separated by coma i.e. 1,2,3.
  --companies COMPANIES
                        The companies to extract information separated by comma i.e. uber.com.
```

Example

```
python app.py --site sitejabber --ratings 1,2,3,4,5 --companies uber.com
```
