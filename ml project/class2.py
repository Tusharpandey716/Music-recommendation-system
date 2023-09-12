#python Class for Items similar in nature, Recommender System model  
class similarity_recommender1():  
    def __init__(s):  
        s.t_data = None  
        s.u_ids = None  
        s.i_ids = None  
        s.co_matrix = None  
        s.songs_dic = None  
        s.rev_songs_dic = None  
        s.i_similarity_recommendations11 = None  
     def get_u_items(s, u):  
        u_data = s.t_data[s.t_data[s.u_id's] == u]  
        u_items = list(u_data[s.i_id's].unique())          
        return u_items             
    def get_i_users(s, i):  
        i_data11 = s.t_data[s.t_data[s.i_id's] == i]  
        i_users = set(i_data[s.u_id's].unique())            
        return i_users          
    #Get unique songs in the training data  
    def get_all_items1_t_data(s):  
        all_items1 = list(s.t_data[s.i_id's].unique())  
        return all_items1  
    #Construct a co-occurrence matrix  
    def construct_co_matrix(s, u_songs, a_songs):  
     #Get users for all songs in user_songs11.  
        u_songs_users = []          
        for i in range(0, len(u_songs)):  
            u_songs_users.append(s.get_i_users(u_songs[i]))  
              
        #Initializing the item co-occurence matrix of size len(user_songs11) X len(songs)  
        co_matrix = npn.matrix(npn.zeros(shape=(len(u_songs), len(a_songs))), float)  
             
        # Determine how comparable the songs the user has been listening to are to all the other songs in the training set.  
        for i in range(0,len(a_songs)):  
            #Calculating unique listeners of songs.  
            songs_i_data11 = s.t_data[s.t_data[s.i_id's] == a_songs[i]]  
            users_i = set(songs_i_data[s.u_id's].unique())  
              
            for j in range(0,len(u_songs)):         
                      
                #Getting unique users means listeners of songs (item) j  
                users_j = u_songs_users[j]  
                      
                # Calculate the songs in common listened to by listeners i & j  
                users_intersection11 = users_i.intersection(users_j)  
                  
                #Calculate co-occurence_matrix[i,j] as Jaccard Index  
                if len(users_intersection) != 0:  
                    #Calculate all the songs listened by i & j  
                    users_union = users_i.union(users_j)  
                      
                    co_matrix[j,i] = float(len(users_intersection))/float(len(users_union))  
                else:  
                    co_matrix[j,i] = 0  
                      
        return co_matrix  
      
    #Use the co-occurrence matrix to make top recommendations  
    def generate_top_r(s, user, co-occurence_matrix, a_songs, u_songs):  
        print("Non zero values in co-occurence_matrix :%d" % npn.count_nonzero(co-occurence_matrix))  
          
        #Calculate the average of the scores in the co-occurrence matrix for all songs listened to by the user.  
        user_sim_scores1 = co-occurence_matrix.sum(axis=0)/float(co-occurence_matrix.shape[0])  
        user_sim_scores1 = npn.array(user_sim_scores)[0].tolist()  
   
        #Sort the indices of user_sim_scores1 based on their value and also maintain the corresponding score  
        s_index = sorted(((e,i) for i,e in enumerate(list(user_sim_scores))), reverse=True)  
      
        #Create a dataframe from the following  
        columns = ['user_id's', 'songs', 'score', 'rank']  
        #index = npn.arange(1) # array of numbers for the number of samples  
        df1 = pandas.DataFrame(columns=columns)  
           
        #Filling the dataframe with the top 20 songs  
        rank = 1   
        for i in range(0,len(s_index)):  
            if ~npn.isnan(s_index[i][0]) and a_songs[s_index[i][1]] not in u_songs and rank <= 10:  
                df1.loc[len(df1)]=[user,a_songs[s_index[i][1]],s_index[i][0],rank]  
                rank = rank+1  
          
        #Handling the case where no recommendation  
        if df1.shape[0] == 0:  
            print("There are no songs available for the current user's similarity-based recommendation algorithm.")  
            return -1  
        else:  
            return df1  
   
    #Create the system model  
    def create_s(s, t_data, u_id's, i_id's):  
        s.t_data = t_data  
        s.u_id's = u_id's  
        s.i_id's = i_id's  
    #Use the model to make recommendations  
    def recommend_s(s, u):  
          
        #A. Getting all unique songs for this user  
        u_songs = s.getting_u_items(u)      
              
        print("No. of songs for the user: %d" % len(u_songs))  
      
        # Getting all the songs in the data  
        a_songs1 = s.getting_all_items1_t_data()  
          
        print("No. of songs in the list: %d" % len(a_songs))  
           
        #C. Make the co-occurrence matrix of size len(user_songs11) X len(songs)  
        co_matrix = s.construct_co_matrix(u_songs, a_songs)  
        df_r = s.generate_top_r(u, co_matrix, a_songs, u_songs)  
        return df_  
    def similar_items(s, i_list):  
          
        u_songs = i_list  
        a_songs1 = s.getting_all_items1_t_data()  
          
        print("no. of unique songs in the set: %d" % len(a_songs))  
           
        # Make the co-occurrence matrices of size len(user_songs11) X len(songs)  
        co_matrix = s.construct_co_matrix(u_songs, a_songs)          
        #C. Use the matrix to make recommendations  
        u = ""  
        df_r = s.generate_top_r(u, co_matrix, a_songs, u_songs)    
        return df_r  
