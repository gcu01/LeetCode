/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeNodes(struct ListNode* head) {
    
    if (head==NULL || head->next==NULL) return NULL; 

    struct ListNode *new_list=(struct ListNode*)malloc(sizeof(struct ListNode)), *new_head;
    new_head = new_list;
    new_list->val = 0;
    bool flag_zero=1;

//for the head
    while(head) {
        if(head->val == 0) {
            head = head->next;
        } else {
            new_list->val += head->val;
            head = head->next;
            if (head && (head->val == 0)) {
                break;
            }
        }
    }

    while (head) {
        if(head->val == 0) {
            head = head->next;
            if (head == NULL) break;
            if (head && (head->val !=0)) flag_zero = 1;
        } else {                
                if (flag_zero == 1) {
                        new_list->next = (struct ListNode*) malloc(sizeof(struct ListNode));
                        new_list = new_list->next;
                        new_list->val = 0;
                        flag_zero = 0;
                }
                new_list->val += head->val;
                head = head->next;
        }
    }

    new_list->next = NULL;

return new_head;
}