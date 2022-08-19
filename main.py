import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

df = pd.read_csv("mma_data.csv")

activites = ['About The Project', 'Visualization and Insights of the Data']
option = st.sidebar.selectbox("Selection option : ", activites)

from PIL import Image

def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

def aboutSection():
	st.title('UFC Fighter Dataset Analysis')
	st.image('mma.jpg')
	st.write('##### About the project')
	st.write('In this project I am researching how the different statistics of mma fighters are related to each other and how they impact the result of a mma match. On this website you will find a summary of my findings. The source of this data is from the ufc fighter list on there website. ')


def visualization():
	st.title('Visualization')
	ques = st.sidebar.radio( "Select the option you want to explore" ,('View Summary of Findings','Explore Findings with more Detail'))
	
	if ques == 'View Summary of Findings':
		st.write("## Summary of Analysis\n\n\n\n")
		st.write('### Key Finding: Fighters who have a speciality in performing takedowns and grappling, consistently have more victories, are able to have higher striking accuracy and absorb less significant strikes over the course of their career. Grapplers are able to more consistently gain a dominanat position on the ground and control the fight from there.')
		st.write('\n\n\n\n')


		st.write("#### Wins By KO")
		fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(12,4))

		fig.subplots_adjust(left=None,
		    bottom=None,
		    right=None,
		    top=None,
		    wspace=0.3,
		    hspace=0.1,)


		sns.scatterplot(x="Striking Accuracy", y="Wins by KO", data = df, ax=axes[0] ,s=130,alpha=0.5);
		sns.scatterplot(x="Takedown Accuracy", y="Wins by KO", data = df, ax=axes[1],s=130, alpha=0.5);

		st.write(fig)

		st.write('Fighters who are better at takedowns get more wins by KO.')
		st.write("\n\n\n\n")



		st.write("#### Wins By Decision")
		fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(12,4))

		fig.subplots_adjust(left=None,
		    bottom=None,
		    right=None,
		    top=None,
		    wspace=0.3,
		    hspace=0.1,)

		sns.scatterplot(x="Striking Accuracy", y="Wins by Decision", data = df, ax=axes[0] ,s=130,alpha=0.5);
		sns.scatterplot(x="Takedown Accuracy", y="Wins by Decision", data = df, ax=axes[1],s=130, alpha=0.5);

		st.write(fig)
		st.write('Fighters who are better at takedowns get more wins by decision.')

		st.write("\n\n\n\n")

		st.write("#### Significant Strike Defense")
		fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(20,10))

		fig.subplots_adjust(left=None,
		    bottom=None,
		    right=None,
		    top=None,
		    wspace=0.3,
		    hspace=0.1,)

		sns.scatterplot(x="Takedown Average", y="Significant strikes Absorbed per minute", data = df, ax=axes[0] ,s=130,alpha=0.5);
		sns.scatterplot(x="Significant strikes per Minute", y="Significant strikes Absorbed per minute", data = df, ax=axes[1],s=130, alpha=0.5);
		st.write(fig)
		st.write("Expert grapplers absorb less strikes over the course of their career in comparison to expert strikers.")



		st.write("\n\n\n\n")

		st.write("#### Win Rate Based on Fighting Expertise.")
		fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(18,5))

		fig.subplots_adjust(left=None,
		    bottom=None,
		    right=None,
		    top=None,
		    wspace=0.3,
		    hspace=0.1,)

		sns.scatterplot(x="Win percentage" , y='Takedown Average', data = df, ax=axes[0] ,s=130,alpha=0.5);
		sns.scatterplot(y="Significant strikes per Minute",x="Win percentage", data = df, ax=axes[1],s=130, alpha=0.5);
		st.write(fig)
		st.write("There is some correlation in the graph on the left indicating that the more skilled a fighter is at performing take downs the higher their win rate becomes. While this correlation also exists regarding the significant strikes landed per minute in the graph on the right, the correlation is stronger in the graph on the left.")



	else:
	
		vis = ['View Correlations', "View Histograms and KDE's"]
		choice = st.sidebar.selectbox("Select Visualization: ", vis)


		
		if (choice=="View Histograms and KDE's"):
			#print("KDE")
			statistics2 = ['Method of Victory', 'Striking Position','Striking Target','Striking and Takedown Accuracy', 'Win Rate', 'Wins and Losses'
			, 'Striking and Takedown Defense', 'Takedown and Submission Average', 'Significant Strikes Absorbed and Landed per Minute', 'Average Fight Time',"Knockdown Average"]

			option = st.sidebar.selectbox("Select MMA Statistic: ", statistics2)

			if option=='Method of Victory':
				fig,axes = plt.subplots(nrows=1,ncols=3, figsize=(12,7))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				#plt.xlim((0,10))
				a =sns.histplot(x="Wins by KO", data = df,  kde=True, ax=axes[0]);
				b =sns.histplot(x="Wins by Submission", data = df,  kde=True, ax=axes[1]);
				c =sns.histplot(x="Wins by Decision", data = df,  kde=True, ax=axes[2]);

				st.write("\n\n\n\n\n Distribution of the different methods of victory of mma fighters")
				st.write(fig)

			elif option=='Striking Position':
				fig,axes = plt.subplots(nrows=1,ncols=3, figsize=(7,4))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				#plt.xlim((0,10))
				a =sns.histplot(x="Standing Position Strikes", data = df,  kde=True, ax=axes[0]);
				b =sns.histplot(x="Clinch Position Strikes", data = df,  kde=True, ax=axes[1]);
				c =sns.histplot(x="Ground Position Strikes", data = df,  kde=True, ax=axes[2]);

				st.write("\n\n\n\n\n Distribution of the different striking positions of mma fighters")
				st.write(fig)

			elif option=='Striking Target':
				fig,axes = plt.subplots(nrows=1,ncols=3, figsize=(8,5))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				
				a =sns.histplot(x="Strikes to Head", data = df,  kde=True, ax=axes[0], bins=40);
				b =sns.histplot(x="Strikes To Body", data = df,  kde=True, ax=axes[1], bins=40);
				c =sns.histplot(x="Strikes To Leg", data = df,  kde=True, ax=axes[2], bins=40);

				st.write("\n\n\n\n\n Distribution of the different striking targets of mma fighters")
				st.write(fig)

			elif option=='Striking and Takedown Accuracy':
				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(7,7))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				#plt.xlim((0,10))
				a =sns.histplot(x="Striking Accuracy", data = df,  kde=True, ax=axes[0]);
				b =sns.histplot(x="Takedown Accuracy", data = df,  kde=True, ax=axes[1]);

				st.write("\n\n\n\n\n Distribution of the striking accuracy and takedown accuracy of mma fighters")
				st.write(fig)

			elif option=='Win Rate':
				fig1, ax = plt.subplots(figsize=(5,5), dpi=200)

				# using the upper triangle matrix as mask 
				a =sns.histplot(x="Win percentage", data = df,  kde=True, ax=ax);

				st.write("\n\n\n\n\n Distribution of the win rates of mma fighters")
				st.write(fig1)

			elif option=='Wins and Losses':

				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(7,7))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				st.write("\n\n\n\n\n Distribution of the wins and losses of mma fighters")
				a =sns.histplot(x="wins", data = df,  kde=True, ax=axes[0]);
				b =sns.histplot(x="losses", data = df,  kde=True, ax=axes[1]);

				st.write(fig)

			elif option=='Striking and Takedown Defense':
				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(7,7))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				st.write("\n\n\n\n\n Distribution of the defensive capabilities of mma fighters")
				a =sns.histplot(x="Significant Strike Defense", data = df,  kde=True, ax=axes[0]);
				b =sns.histplot(x="Takedown Defense", data = df,  kde=True, ax=axes[1]);

				st.write(fig)

			elif option=='Takedown and Submission Average':
				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(7,7))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				st.write("\n\n\n\n\n Distribution of the grappling capabilities of mma fighters")
				a =sns.histplot(x="Takedown Average", data = df,  kde=True, ax=axes[0]);
				b =sns.histplot(x="Submission Average", data = df,  kde=True, ax=axes[1]);
				a.set(xlim=(0, 8))
				b.set(xlim=(0, 4))

				st.write(fig)

			elif option=='Significant Strikes Absorbed and Landed per Minute':
				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(7,7))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				sns.histplot(x="Significant strikes per Minute", data = df,  kde=True, ax=axes[0]);
				sns.histplot(x="Significant strikes Absorbed per minute", data = df,  kde=True, ax=axes[1], bins=10);

				plt.xlim((0,25))

				st.write("\n\n\n\n\n Distribution of the striking capabilities of mma fighters")
				st.write(fig)

			elif option=='Average Fight Time':
				fig1, ax = plt.subplots(figsize=(5,5), dpi=200)

				# using the upper triangle matrix as mask 
				a =sns.histplot(x='Average Fight Time', data = df,  kde=True, ax=ax);

				st.write("\n\n\n\n\n Distribution of the fight times of mma fighters")
				st.write(fig1)

			elif option=="Knockdown Average":
				fig1, ax = plt.subplots(figsize=(5,5), dpi=200)

				# using the upper triangle matrix as mask 
				a =sns.histplot(x="Knockdown Average", data = df,  kde=True, ax=ax);

				st.write("\n\n\n\n\n Distribution of the knockdown averages of mma fighters")
				st.write(fig1)



		else:

			statistics = ['Takedown Average', 'Significant Strike Defense', 'Total Fights', 'Takedown Defense'
			, 'Knockdown Average', 'Average Fight Time', 'Win by Submission', 'Wins By Decision'
			,'Strikes To The Head', 'Striking Accuracy', 'Wins By KO', 'Striking and Takedown Accuracy ', 'Wins by Decision']

			option = st.sidebar.selectbox("Select MMA Statistic: ", statistics)


			if (option == 'Takedown Average'):
				st.write("### Statistic Correlation")
				
				fig, ax = plt.subplots(figsize=(8,8), dpi=200)
				sns.scatterplot(x='Takedown Average',y='Significant strikes Absorbed per minute',data=df, s=100, alpha=0.5, ax=ax)
				st.write(fig) 

				st.write("### Explaination of Correlation")
				st.write("##### There is a negative correlation indicating that as the amount of takedowns a fighter can land over a 15 minute period increases the amount of significant strikes the fighter absorbs decreases. This is most likely because a fighters who can land takedowns more consistently are more likely able to gain a dominanat position where their opponenet cannot hit them easily. This may also indicate that mastering the ability takedown an opponent and having a strategy that focuses on the takedown is good if fighters want to avoid taking damage and increase the longevity of their career as it appears that fighters who have a high of amount of takedown skill get hit less. ")
			
			elif (option == 'Significant Strike Defense'):
				_max_width_()

				st.write("### Statistic Correlation")
				
				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(12,7))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				sns.scatterplot(x="Significant Strike Defense", y="Takedowns Attempted", data = df, ax=axes[0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Significant Strike Defense", y="Strikes Attempted", data = df, ax=axes[1],s=130, alpha=0.5);
				st.write(fig) 

				st.write("### Explanation of Correlation")
				st.write("##### Fighters with higher significant strike defense are able to accumalate more total takedown and striking attempts than other fighters across their career. This means that having better significant strike defense can lead a fighter to having a longer career, and participating in more fights.")
			elif(option == 'Total Fights'):

				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(10,5))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				# axes[0].plot("Significant Strike Defense", "Takedowns Attempted", data = df)
				# axes[1].plot("Significant Strike Defense", "Strikes Attempted", data=df)

				sns.scatterplot(x="Significant Strike Defense", y="Total Fights", data = df, ax=axes[0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Takedown Defense", y="Total Fights", data = df, ax=axes[1],s=130, alpha=0.5);
				st.write(fig) 
				
				st.write("### Explanation of Correlation")
				st.write("##### Some correlation indicating fighters with better significant strike defense and takedown are able to participate in more fights meaning that a better significant strike defense can imporve the longevity of a fighter.")		
			
			elif(option == 'Takedown Defense'):
				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(8,8))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				# axes[0].plot("Significant Strike Defense", "Takedowns Attempted", data = df)
				# axes[1].plot("Significant Strike Defense", "Strikes Attempted", data=df)

				sns.scatterplot(x="Takedown Defense", y="Significant strikes per Minute", data = df, ax=axes[0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Takedown Defense", y="Submission Average", data = df, ax=axes[1],s=130, alpha=0.5);
			
				st.write(fig) 

				st.write("### Explanation of Correlation")
				st.write("##### This reveals that a common strategy among ufc fighters. The striking specialists and really good strikers typically have good takedownn defense because they want to only strike not wrestle so they avoid it all together by having really good TD defense.")

			elif(option == 'Knockdown Average'):
				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(8,8))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				# axes[0].plot("Significant Strike Defense", "Takedowns Attempted", data = df)
				# axes[1].plot("Significant Strike Defense", "Strikes Attempted", data=df)

				sns.scatterplot(x="Knockdown Average", y="Significant strikes per Minute", data = df, ax=axes[0] ,s=130,alpha=0.5);
				sns.scatterplot(y="Takedown Defense", x="Knockdown Average", data = df, ax=axes[1],s=130, alpha=0.5);

				st.write(fig)

				st.write("### Explanation of Correlation")
				st.write("##### Fighters with higher knockdown averages seem to have higher Takedown defense and Significant str per minute. Fighters with really high knockdown average have really good takedown defense meaning really good strikers don't want to wrestle and want to avoid it by defending the takedown as much as possible")

			elif(option == 'Average Fight Time'):
				fig,axes = plt.subplots(nrows=2,ncols=2, figsize=(8,8))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)


				sns.scatterplot(x="Average Fight Time", y="Takedowns Attempted", data = df, ax=axes[0][0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Average Fight Time", y="Significant Strike Defense", data = df, ax=axes[0][1],s=130, alpha=0.5);
				sns.scatterplot(x="Average Fight Time", y="Wins by Submission", data = df, ax=axes[1][0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Average Fight Time", y="Knockdown Average", data = df, ax=axes[1][1],s=130, alpha=0.5);

				st.write(fig)

				st.write("### Explanation of Correlation")

				st.write("##### Higher fight time means fighters might be looking for submissions more, and people with higher fight times is correlated to fighters attempting more takedowns. This means that fighters whose strategy, skills revolve around takedowns are likely to have a longer fight. ")
				st.write("##### People with higher fight times are more likely to have more wins by submission. This means that as the fight time gets longer it is more likely to favor the fighter who has expertise performing submissions. This is because submissions take time to setup and complete")
				st.write("##### As the average fight time for a fighter increases it is less that a fighter has a high knockdown average. This means that most fighters with high average fight times are most likely not expert strikers, and that expert strikers do not want for the fight to last longer and want it to be completed quickly. This is most likely because expert strikers rely on explosive energy to perform powerful strikes which significantly decreases as the fight gets longer which is not in their favor.")

			elif(option == 'Win by Submission'):
				fig,axes = plt.subplots(nrows=2,ncols=2, figsize=(8,8))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)


				sns.scatterplot(x="Wins by Submission", y="Average Fight Time", data = df, ax=axes[0][0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Wins by Submission", y="Significant Strike Defense", data = df, ax=axes[0][1],s=130, alpha=0.5);
				sns.scatterplot(x="Wins by Submission", y="Knockdown Average", data = df, ax=axes[1][0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Wins by Submission", y="Takedowns Attempted", data = df, ax=axes[1][1],s=130, alpha=0.5);

				st.write(fig)

				st.write("### Explanation of Correlation")

				st.write("##### Once again fighters with a lot of wins by submission have a higher average fight time. This means a longer fight is in their benefit. This is most likely because submissions take time to setup and work better when their opponent is tired which can be achieved with lengthier fights.")
				st.write("##### We can see that fighters with a speciality in submission have excellent significant striking defense which is mostly likely because they want to grapple and not strike in the fight. So they will avoid it by having good striking defense.")
				st.write("##### Fighters with more wins by submission appear to have higher significant strike defense. This is most likely because the strategy of the fighter revovlves around their grappling and they do not plan to use their striking too much to help inflict damage on their opponent. As a result they focus heavily on being able to defend from strikes so they do not get KOed and can go forward to use their grappling.")
				st.write("### Most grappling specialists do not have as much expertise on striking. Their game plan revolves around their grappling and as a result they do not strike as much meaning they do not score a lot of knockdowns which is why their knockdown average is lower the more wins by submission a fighter has.")

			elif(option=='Wins By Decision'):

				fig, ax = plt.subplots(figsize=(5,5), dpi=200)
				
				sns.scatterplot(x="Wins by Decision" , y='Submission Average', data=df,s=130,alpha=0.3, ax=ax );
				
				st.write(fig)
				st.write("### Explanation of Correlation")
				st.write("##### There is a correlation  that indicates that the more wins a fighter has by decision the higher a submission average the fighter has. This means that fighters whose strategy, and specialities are in submissions eithier get the win by submission or held enough dominanace over their opponent to get the win by decision. So if a fighter is mostly specilaised in grappling longer fights favor them.")
				

			elif(option =='Strikes To The Head'):
				fig, ax = plt.subplots(figsize=(5,5), dpi=200)
				sns.scatterplot(x="Strikes to Head" , y='Takedowns Attempted', data=df,s=130,alpha=0.3 )
				st.write(fig)

				st.write("### Explanation of Correlation")
				st.write("##### This plot shows that fighters have accumalated a lot of strikes to head also attempt a lot of takedowns. This is indicative of a stratgey that appears to be common in mma fights. The strategy is for fighters to throw several strikes to the head and then one time fake a strike to the head and go for a easy takedown. This means that fighers who has an opponent who is good at takedowns should be aware that this strategy can be used against them.")
				st.write("##### It also may indicate that hitting the head is a lot easier once the fighter is taken to the ground.")

			elif(option == 'Striking Accuracy'):

				fig,axes = plt.subplots(nrows=2,ncols=2, figsize=(8,8))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				sns.scatterplot(x="Striking Accuracy", y="Ground Position Strikes", data = df, ax=axes[0][0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Striking Accuracy", y="Knockdown Average", data = df, ax=axes[1][0],s=130, alpha=0.5);
				sns.scatterplot(x="Striking Accuracy", y="Standing Position Strikes", data = df, ax=axes[0][1] ,s=130,alpha=0.5);
				sns.scatterplot(x="Striking Accuracy", y="Takedown Average", data = df, ax=axes[1][1],s=130, alpha=0.5);

				st.write(fig)

				st.write("### Explanation of Correlation")
				st.write("##### Fighters with higher striking accuracy have accumalated a higher number of ground positon strikes. This means that when a fighter is striking an opponenet in a grounded possition they can do it with a high level of accuracy. This most likely consists of fighters whose expertise is grappling as they will be the fighetrs who can establish a dominant ground position to deliver these high accuracy ground strikes. ")
				st.write("##### This shows that fighters who have a high striking accuracy actually perform less strikes from the standing possition indicating that the fighters with the highest striking accuracy are not actually a majority of striking experts but a majority of grappling experts")

				
				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(9,9))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				sns.scatterplot(x="Striking Accuracy", y="wins", data = df, ax=axes[0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Striking Accuracy", y="losses", data = df, ax=axes[1],s=130, alpha=0.5);

				st.write(fig)
					
				st.write("### Explanation of Correlation")
				st.write("##### There is little correlation between striking accuracy and wins and strking accuracy and losses indicating that fighters who are striking experts have more inconsistent outcomes to their matches.")

			elif(option == 'Wins By KO'):
				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(7,7))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				sns.scatterplot(x="Striking Accuracy", y="Wins by KO", data = df, ax=axes[0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Takedown Accuracy", y="Wins by KO", data = df, ax=axes[1],s=130, alpha=0.5);

				st.write(fig)

				st.write("### Explanation of Correlation")
				st.write("##### Here it can be seen that there is little to no correlation between the accuracy of a striker and the amount of wins they have by KO. But there is some correlation between takedown accuracy and Wins by KO on the right. This means that fighters who have expertise in the takedown are more likely to get a KO than fighters who specialize in striking. ")

			elif(option == 'Wins by Submission'):
				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(7,7))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				sns.scatterplot(x="Striking Accuracy", y="Wins by Submission", data = df, ax=axes[0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Takedown Accuracy", y="Wins by Submission", data = df, ax=axes[1],s=130, alpha=0.5);

				st.write(fig)

				st.write("### Explanation of Correlation")
				st.write("##### There is some correlation in the second graph showing fighters with higher takedown accuracy are more likely to win by submission as a fighter who can succesfully perform a takedown can more often put themself in a good position to perform a submission.")

			elif(option == 'Wins by Decision'):

				fig,axes = plt.subplots(nrows=1,ncols=2, figsize=(14,7))

				fig.subplots_adjust(left=None,
				    bottom=None,
				    right=None,
				    top=None,
				    wspace=0.3,
				    hspace=0.1,)

				sns.scatterplot(x="Striking Accuracy", y="Wins by Decision", data = df, ax=axes[0] ,s=130,alpha=0.5);
				sns.scatterplot(x="Takedown Accuracy", y="Wins by Decision", data = df, ax=axes[1],s=130, alpha=0.5);

				st.write(fig)

				st.write("### Explanation of Correlation")
				st.write("##### Some correlaition in the secnd graph showing fighters with higher takedown accuracy are more liley to win by decision as a fighter who can succesfully perform a takedown can more often can hold a dominanat position for a longer period of time in the fight resulting in a win by decision.")


		heatmap = st.sidebar.checkbox("Display Heatmap of the data")

		if (heatmap):


			fig1, ax = plt.subplots(figsize=(18,18), dpi=200)
			
			corr= df.corr()

			# Getting the Upper Triangle of the co-relation matrix
			matrix = np.triu(corr)

			# using the upper triangle matrix as mask 
			sns.heatmap(corr, annot=True, mask=matrix, ax=ax)

			st.write(fig1)


if(option=='About The Project'):
	aboutSection()
elif(option=='Visualization and Insights of the Data'):
	visualization()
