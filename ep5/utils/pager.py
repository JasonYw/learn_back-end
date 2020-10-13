class PageInfo(object):
    def __init__(self,current_page,per_page,all_conut,show_page,href_):
        self.per_page =per_page
        self.all_conut =all_conut
        self.show_page =show_page
        self.all_pager,b =divmod(self.all_conut,self.per_page)
        self.href_ =href_
        if b:
            self.all_pager =self.all_pager+1 
        try:
            self.current_page =int(current_page)
            if self.current_page<= 0 or self.current_page>self.all_pager:
                raise ArithmeticError
        except:
            self.current_page =1
        
    def start(self):
        return (self.current_page-1)*self.per_page

    def end(self):
        return self.current_page*self.per_page
    
    def pager(self):
        pager_list =[]
        begin =self.current_page -int((self.show_page-1)/2)
        stop =self.current_page +int((self.show_page-1)/2) +1
        if self.all_pager <= self.show_page:
            begin =1
            stop=self.all_pager+1
        else:
            if begin <=0 or stop <=0:
                begin =1
                stop =11
            if begin > self.all_pager or stop > self.all_pager:
                begin =self.all_pager-10
                stop =self.all_pager+1
        
      
        prev='<li><a href="%s?page=%s" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'%(self.href_,self.current_page-1)
        pager_list.append(prev)
        for page in range(begin,stop):
            if int(page) == self.current_page:
                pager_list.append(f'<li class="active" ><a href="{self.href_}?page={page}">{page}</a></li>')
            else:
                pager_list.append(f'<li><a href="{self.href_}?page={page}">{page}</a></li>')
        next_page ='<li><a href="%s?page=%s" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'%(self.href_,self.current_page+1)
        pager_list.append(next_page)
        return ''.join(pager_list)


    