SELECT JSONExtractString(
		replaceAll(
			replaceOne(replaceOne(failures, '{"', ''), '}"', ''),
			'\\',
			''
		),
		'reason'
	) as,
	date_utc,
	FROM db_spacex.launches
WHERE NOT success