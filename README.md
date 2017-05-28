# Creighton-Model-Chart

[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](https://github.com/mkudija/Creighton-Model-Chart/blob/master/LICENSE)
[![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&maxAge=2592000)](https://twitter.com/mkudija)

> Plotting of Creighton Model charts.

---

## Example Chart
![Example](https://github.com/mkudija/Creighton-Model-Chart/blob/master/Charts/example1.png)

## Disclaimer
This software is not endorsed or in any way affiliated with the Pope Paul VI Institute or the "Official Creighton Model". It is intended only to facilitate electronic vizualization instead of paper charts with physical stickers. The user provides determination of what to chart via data files in [`Data/`](https://github.com/mkudija/Creighton-Model-Chart/tree/master/Data). 

## Background
According to the [United States Conference of Catholic Bishops](http://www.usccb.org/issues-and-action/marriage-and-family/natural-family-planning/what-is-nfp/), Natural Family Planning (NFP) is "the general title for the scientific, natural and moral methods of family planning that can help married couples either achieve or postpone pregnancies."

The [Creighton Model](http://www.creightonmodel.com/index.html) is one of several NFP methods which uses the observation of biomarkers (cervical mucus) to identify the natural times of fertility and infertility. Other popular methods include [the Billings Model](http://www.woomb.org/), [the Sympto-Thermal Method](https://sympto.org/data/manual_en_sympto.pdf), and [the Marquette Model](http://nfp.marquette.edu/), with information about other methods [here](http://www.usccb.org/issues-and-action/marriage-and-family/natural-family-planning/what-is-nfp/methods.cfm) and [here](http://verilymag.com/2016/12/how-to-chart-your-cycle-creighton-billings-two-day-sympto-thermal-marquette-lactational). The [Creighton Model](http://www.unleashingthepower.info/PDFs/IA_IntroCrMS.pdf) was developed by Dr. Thomas Hilgers at Creighton University in the 1970's and 1980's and is one of the most popular NFP methods. It has been widely studied, and has also led to the development of NaProTechnology (natural procreative technology), a method of medical treatments for women that preserves fertility.

Charting is a convenient way of visually tracking the woman's cycle. Creighton Method instruction typically includes instruction in using a paper chart (examples of which are available [here](http://www.creightonmodel.com/background.htm)). Unfortunately, there does not appear to be an app or other form of electronic charting offered by any organization officially affiliated with Creighton. Electronic charting in some form would greatly improve convenience and data integrity.

### Survey of Electronic Charting Options
There are a variety of electronic (app, online, spreadsheet) charting options available offering various combinations of features and degrees of compatibility with the Creighton model. Below are links to some of the options I found online:

#### Charting Apps
* [NFP Charting (free)](https://itunes.apple.com/us/app/nfp-charting/id300767738?mt=8)
* [Kindara (free)](https://www.kindara.com/)
* [OvuView (free)](https://play.google.com/store/apps/details?id=com.sleekbit.ovuview&hl=en)
* [Ovia Fertility Tracker (free)](https://itunes.apple.com/us/app/ovia-fertility-tracker-ovulation-calculator/id570244389?mt=8)
* [Lily (free)](http://whimsicallily.com/lily/appstore.php)
* [Fertility Friend (free)](https://itunes.apple.com/app/apple-store/id443919067?mt=8)

#### Online Charting
* [Northwest Family Services ($12)](http://www.nwfs.org/natural-family-planning/online-charting)
* [My Fertility Charts ($2.50/mo)](http://www.myfertilitycharts.com/)

#### Homemade Electronic Charts
* [Creighton Model of Natural Family Planning Digital Chart (Google Sheets)](http://nfpandme.blogspot.com/2012/03/good-bye-paper-charts.html)

## Creighton-Model-Chart
Finding nothing that meets our needs above, and wanting to make something simple in Python, I generated these scripts. This provides a simple way of visualizing biomarker observations.

### Stickers
<img src="https://github.com/mkudija/Creighton-Model-Chart/blob/master/Stickers/g.png" width="50"/> <img src="https://github.com/mkudija/Creighton-Model-Chart/blob/master/Stickers/r.png" width="50"/> <img src="https://github.com/mkudija/Creighton-Model-Chart/blob/master/Stickers/y.png" width="50"/> <img src="https://github.com/mkudija/Creighton-Model-Chart/blob/master/Stickers/gb.png" width="50"/> <img src="https://github.com/mkudija/Creighton-Model-Chart/blob/master/Stickers/gb1.png" width="50"/> <img src="https://github.com/mkudija/Creighton-Model-Chart/blob/master/Stickers/gb2.png" width="50"/> <img src="https://github.com/mkudija/Creighton-Model-Chart/blob/master/Stickers/gb3.png" width="50"/> <img src="https://github.com/mkudija/Creighton-Model-Chart/blob/master/Stickers/wb.png" width="50"/> <img src="https://github.com/mkudija/Creighton-Model-Chart/blob/master/Stickers/wbp.png" width="50"/>

Images to form the "stickers" are located in [`/Stickers`](https://github.com/mkudija/Creighton-Model-Chart/tree/master/Stickers). Stickers with the baby illustration are derived from the "dancing baby" by [Jeff Geerling](https://www.jeffgeerling.com/blog/2010/dancing-baby-illustration). 

### Usage

#### Installation
Clone this repo using [`https://github.com/mkudija/Creighton-Model-Chart.git`](https://github.com/mkudija/Creighton-Model-Chart.git).

#### Requirements

* python 3.5.2
* matplotlib 1.5.1
* pandas 0.18.1


#### Generate Data
User inputs are gathered via Excel files in [`Data/`](https://github.com/mkudija/Creighton-Model-Chart/tree/master/Data). 

| Date          | Discharge     | Sticker  | Intercourse  | 
| ------------- |:-------------:| -------- | ------------ |
| MM/DD/YY      | *record using usual code* | *see below* | Record **I** for Intercourse | 

**Stickers** - use the following codes for each sticker type:
- `g` - green
- `r` - red
- `y` - yellow
- `wb` - white baby
- `wbp` - white baby (Peak Day)
- `wb1` - white baby (Peak +1)
- `wb2` - white baby (Peak +2)
- `wb3` - white baby (Peak +3)
- `gb` - green baby 
- `gb1` - green baby (Peak +1)
- `gb2` - green baby (Peak +2)
- `gb3` - green baby (Peak +3)


#### Create Single Chart
Run [`(1)plotChart.ipynb`](https://github.com/mkudija/Creighton-Model-Chart/blob/master/(1)plotChart.ipynb) to generate the chart for a single cycle. Note that the filepaths reference local directories to protect privacy. Change filepaths as needed to the location of your data and desired output for charts. Update `name` for the date of the start of the cycle you want to plot. 

#### Merge Charts
Run [`(2)combineCharts.ipynb`](https://github.com/mkudija/Creighton-Model-Chart/blob/master/(2)combineCharts.ipynb) to combine multiple single cycle charts into a full chart (the group of 6 cycles you are used to seeing on paper charts). Again, change paths as required to match your directory of individual charts, and update `list_im` with the individual charts you wish to include.  

