SELECT JSONExtractString(
		replaceAll(
			replaceOne(replaceOne(failures, '{"', ''), '}"', ''),
			'\\',
			''
		),
		'reason'
	) as reason,
	date_utc,
	FROM db_spacex.launches
WHERE NOT success