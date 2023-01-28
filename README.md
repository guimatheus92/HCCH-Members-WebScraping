# HCCH Members WebScraping

![HCCH](https://user-images.githubusercontent.com/11640754/215232766-7f9f68de-f449-41c5-9882-1e3708780461.png)

This Python script basically enters the URL https://www.hcch.net/en/states/hcch-members, to get all the HCCH member countries, and adds them all into a dataframe with their respective links and language in which the site was fetched.

Therefore, just change the urls of the variables below:

`base_url = "https://www.hcch.net"`
`urls = ["https://www.hcch.net/pt/states/hcch-members/", "https://www.hcch.net/en/states/hcch-members/"]`

After that, you will get a dataframe similar to this:

|  DT_RUN | NM_COUNTRY  | DS_COUNTRYLINK | NM_WEBSITELANGUAGE  | DS_SOURCELINK  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
|  27/01/2023 | Albania  |  https://www.hcch.net/en/states/hcch-members/details1/?sid=18 | en  |  https://www.hcch.net/en/states/hcch-members/ |
|  27/01/2023 | Andorra  | https://www.hcch.net/en/states/hcch-members/details1/?sid=79  |  en | https://www.hcch.net/en/states/hcch-members/  |
|  27/01/2023 | Argentina | https://www.hcch.net/en/states/hcch-members/details1/?sid=20  | en  | https://www.hcch.net/en/states/hcch-members/  |
| 27/01/2023  |  Armenia | https://www.hcch.net/en/states/hcch-members/details1/?sid=81  | en  |  https://www.hcch.net/en/states/hcch-members/ |
