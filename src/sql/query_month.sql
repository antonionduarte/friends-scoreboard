SELECT score, user_id, entry_date FROM entry
WHERE entry_date >= ? AND entry_date <= ? 
AND user_id = ?;
