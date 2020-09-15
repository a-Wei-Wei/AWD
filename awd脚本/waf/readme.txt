drop_waf 功能为 日志抓取和waf
waf-1 这个下面的waf 比较强
两者部署的方式均为找到php 应用的入口文件，include_once 引入即可，但是可能waf太强会导致check失败，所以谨慎使用，或者修改waf的检测规则