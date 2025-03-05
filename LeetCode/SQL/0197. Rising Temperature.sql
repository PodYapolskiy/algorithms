select
    today.id
from
    weather as today
join
    weather as yesterday
on
    today.recordDate = yesterday.recordDate + interval '1 day'
where
    today.temperature > yesterday.temperature    
