/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {

    if (head == NULL || head->next == NULL) return head;

    struct ListNode *curr = head, *prev;
    bool flag = 0;

//finding the head
    while(curr != NULL) {
        if (curr->next != NULL && curr->next->val == head->val) {
            curr = curr->next; flag = 1;
        } else if (flag == 1) {
            curr = curr->next;
            head = curr;
            flag = 0;
            if ( curr && curr->next != NULL && curr->next->val > curr->val) break;
        } else break;
    }
    if (head == NULL) return head;
    //if ( curr) printf("\n head->val = %d", head->val);
    prev = head;

    while(curr->next != NULL) {
        if (curr->next->val == curr->val) {
            curr = curr->next; 
            if (curr->next == NULL) {
                prev->next = NULL;
                break;
            }
        } else {
            curr = curr->next;
            prev->next = curr;

            if (curr && curr->next != NULL && curr->next->val > curr->val) {
                prev = curr;
            }
        } 

    }
//printf("\n curr->val = %d curr->next->val = %d", curr->val, curr->next->val);



// too complex
/*
    //find the head
    while (curr->next != NULL && curr->next->val == curr->val) {
        curr = curr->next;
        flag = 1;
    }
    
    if (flag) {
        curr = curr->next;
        prev = curr;
        head = curr;
        flag = 0;
    }
    if (curr == NULL) return NULL;
    printf("\n prev->val = %d", prev->val);
//printf("\n head->val = %d", head->val);
    while (curr->next != NULL) {
        if (curr->next->val > curr->val) {
            
            if (odd == 1 ) {
                prev = curr;
                curr = curr->next;
                odd = 0;
            } else {
                curr = curr->next;
                odd++;
            }
  
        } else {
            printf("\n curr = %p", curr);
            
            printf("\n prev->val = %d", prev->val);
            while (curr->next->val == curr->val) {
                curr = curr->next;
                if (curr->next == NULL && prev->val == curr->val) return NULL;
                if ( curr->next == NULL) { 
                    prev->next = NULL;
                    return head;
                }
                flag = 1;
            }
            if (flag) {
                curr = curr->next;
                prev->next = curr;
                //prev = curr;
                flag = 0;
                odd = 0;
            }
        }

    }
 */   
    return head;
}