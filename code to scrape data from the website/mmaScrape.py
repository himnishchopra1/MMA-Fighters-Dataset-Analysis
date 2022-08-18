import scrapy
import logging



class UfcscrapeSpider(scrapy.Spider):
    name = 'ufcScrape'
    
    # URL I scrpaed data from
    allowed_domains = ['www.ufc.com']
    start_urls = ['https://www.ufc.com/athletes/all']


    # response from scrape is recevived in this method
    def parse(self, response):

        fighters = response.xpath("//div[@class='c-listing-athlete-flipcard__inner']")

        # Parsing data to select correct url that contains fighter data
        for fighter in fighters:

            name = fighter.xpath("normalize-space(.//div[@class='c-listing-athlete-flipcard__front']/div[@class='c-listing-athlete__text']/span[@class='c-listing-athlete__name']/text())").get()
            link = fighter.xpath(".//div[@class='c-listing-athlete-flipcard__back']/div[@class='c-listing-athlete-flipcard__action']/a/@href").get()
            url = response.urljoin(link)

            # yield {
            #     'name': name,
            #     'url': url
            # }
            yield response.follow(url=link, callback=self.parse_fighter)


        next_page = response.urljoin(response.xpath("//li[@class='pager__item']/a/@href").get())

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

        
    # Method to select the data features
    def parse_fighter(self, response):
       # logging.info(response.url)

        name = response.xpath("//h1[@class='hero-profile__name']/text()").get()
        
        #Wins-Losses-Draws
        wld = response.xpath("//p[@class='hero-profile__division-body']/text()").get()

 

        ST = response.xpath("//dd[@class='c-overlap__stats-value']")
        strikesLanded=0
        strikesAtempted=0
        takedownsLanded=0
        takedownsAttempted=0        
        if ST is not None:
            i = 0
            for val in ST:
                if i==0:
                    strikesLanded = val.xpath(".//text()").get()
                elif i==1:
                    strikesAtempted = val.xpath(".//text()").get()
                elif i==2:
                    takedownsLanded = val.xpath(".//text()").get()
                elif i==3:
                    takedownsAttempted = val.xpath(".//text()").get()
                i=i+1

        stats2 = response.xpath("//div[@class='c-stat-compare__number']")
        
        SigStrikesLandedPerMinute = 0
        SigStikesAbsorbedPerMinute = 0
        TakedownAvg = 0
        SubmissionAvg = 0
        SigStrikeDefense= 0
        TakedownDefense = 0
        KnockdownAvg = 0
        AvgFightTime = 0

        if stats2 is not None:
            i = 0
            for num in stats2:       
                if i==0:
                    SigStrikesLandedPerMinute = num.xpath("normalize-space(.//text())").get()
                elif i==1:
                    SigStikesAbsorbedPerMinute = num.xpath("normalize-space(.//text())").get()
                elif i==2:
                    TakedownAvg = num.xpath("normalize-space(.//text())").get() #Amount of takedowns attempted i guess per 15 mins
                elif i==3:
                    SubmissionAvg = num.xpath("normalize-space(.//text())").get()
                elif i==4:
                    SigStrikeDefense= num.xpath("normalize-space(.//text())").get()
                elif i==5:
                    TakedownDefense = num.xpath("normalize-space(.//text())").get()
                elif i==6:
                    KnockdownAvg = num.xpath("normalize-space(.//text())").get()
                elif i==7:
                    AvgFightTime = num.xpath("normalize-space(.//text())").get()
                i+=1
                
        #Significant strike by position
        stats3 = response.xpath("//div[@class='c-stat-3bar__value']")
        standingStrike = 0
        clinchStrike = 0
        groundStrike = 0
        winMethodKO = 0
        winMethodSub = 0
        winMethodDec = 0

        if stats3 is not None:
            i = 0
            for num in stats3:       
                if i==0:
                    standingStrike = num.xpath("normalize-space(.//text())").get()
                elif i==1:
                    clinchStrike = num.xpath("normalize-space(.//text())").get()
                elif i==2:
                    groundStrike = num.xpath("normalize-space(.//text())").get() 
                elif i==3:
                    winMethodKO = num.xpath("normalize-space(.//text())").get() 
                elif i==4:
                    winMethodSub = num.xpath("normalize-space(.//text())").get() 
                elif i==5:
                    winMethodDec = num.xpath("normalize-space(.//text())").get() 
                
                i+=1


        strikesToHead = response.xpath("//*[@id='e-stat-body_x5F__x5F_head_value']/text()").get()
        strikesToBody = response.xpath("//*[@id='e-stat-body_x5F__x5F_body_value']/text()").get()
        strikesToLeg = response.xpath("//*[@id='e-stat-body_x5F__x5F_leg_value']/text()").get()


        # getting all fetures of each fighter and placing them in a csv file
        yield {
            'name': name,
            'wins_losses_draw': wld,
            "Strikes Landed" : strikesLanded,
            "Strikes Attempted" : strikesAtempted,
            "Takedowns Landed": takedownsLanded,
            "Takedowns Attempted" : takedownsAttempted,
            "Significant strikes per Minute": SigStrikesLandedPerMinute,
            "Significant strikes Absorbed per minute":SigStikesAbsorbedPerMinute,
            "Takedown Average": TakedownAvg,
            "Submission Average":SubmissionAvg,
            "Significant Strike Defense": SigStrikeDefense,
            "Takedown Defense":TakedownDefense,
            "Knockdown Average": KnockdownAvg,
            "Average FIght Time": AvgFightTime,
            "Standing Position Strikes":standingStrike,
            "Clinch Position Strikes":clinchStrike,
            "Ground Position Strikes":groundStrike,
            "Wins by KO":winMethodKO,
            "Wins by Submission":winMethodSub,
            "Wins by Decision":winMethodDec,
            "Strikes to Head":strikesToHead,
            "Strikes To Body":strikesToBody,
            "Strikes To Leg":strikesToLeg
        }

            #yield scrapy.Request(url=url)

    



