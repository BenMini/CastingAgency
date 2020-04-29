

@app.route('/actors', methods=['GET', 'POST'])
@app.route('/actors/<actor_id>', methods=['PATCH', 'DELETE'])
@app.route('/movies', methods=['GET', 'POST'])
@app.route('/movies/<actor_id>', methods=['PATCH', 'DELETE'])
