def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        slow=head
        fast=head 
        f=False
        while fast and fast.next: 
            slow=slow.next 
            fast=fast.next.next 
            if slow==fast: 
                f=True 
                break 
        if f==False: 
            return None
        fast=head 
        while slow!=fast: 
            fast=fast.next 
            slow=slow.next 
        return slow
