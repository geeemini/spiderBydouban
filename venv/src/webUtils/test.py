import random
sql = 'insert into movie_from_db (id, url, name, area, year, score, type, time ) values (26877406,"https://movie.douban.com/j/subject_abstract?subject_id=26877406","名侦探柯南：章节ONE 变小的名侦探 名探偵コナン エピソード "ONE" 小さくなった名探偵‎ (2016)","日本","2016","8.3","动画,悬疑","2019-10-29 09:07:31")'
sql = sql.replace('"','\\"')
rnd = round(random.uniform(1, 3),2)
print(sql)