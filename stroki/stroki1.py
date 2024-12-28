def search_substr(subst,st):
    subst = subst.lower()
    st = st.lower()
    if subst in st:
        print ("Есть контакт!")
    else:
        print ("Мимо!")

search_substr("abc","ytvboABCunrc")
search_substr("abc","bvlbpefiahpurfovr")
