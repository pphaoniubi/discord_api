import pandas as pd
import matplotlib.pyplot as plt


outfile = 'Discord.csv'
df = pd.read_csv(outfile)



df['Time'] = pd.to_datetime(df['Time'])

# Filter the DataFrame for the year 2023
df_2023 = df[df['Time'].dt.year == 2023]

df_2023['Username'].value_counts().nlargest(8).plot.bar(figsize=(8,8))

df['Month'] = df['Time'].dt.month

plt.title('ggnohelp 2023 Top Message Sender')
plt.xlabel('Count')
plt.xticks(rotation=40)
plt.ylabel('User')
plt.legend()
plt.savefig('{}_Message.png'.format(outfile.replace('.csv', '')))
plt.close()

df_2023['Month'] = df_2023['Time'].dt.month
df_2023['Year'] = df_2023['Time'].dt.year

# Group by User, Year, and Month and count the messages
message_counts_2023 = df_2023.groupby('Month').size().reset_index(name='Message_Count')

plt.bar(message_counts_2023['Month'], message_counts_2023['Message_Count'])
plt.xlabel('Month')
plt.ylabel('Message Count')
plt.title('ggnohelp 2023 message count per Month')
plt.savefig('{}_ByMonth'.format(outfile.replace('.csv', '')))