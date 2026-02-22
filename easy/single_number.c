#include<stdio.h>
#include<stdlib.h>

struct Node{
    int num;
    struct Node *next;
};

typedef struct Node* List;

int singleNumber(int* nums, int numsSize);
void addToList(List *head, List *tail, int n);
int removeFromListIfExists(List *head, List *tail, int n);
void printList(List head);


int main(){

    //int arr[] = {4,1,2,1,2};
    //int arr[] = {2,2,1};
    int arr[] = {1,1,2,3,4,5,4,5,3,-1,2};
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    int num = singleNumber(arr,arr_size);

    printf("%d\n",num);

    return 1;
}

int singleNumber(int* nums, int numsSize) {
    List head = NULL;
    List tail = NULL;
    for(int i=0;i<numsSize;i++){
        if(removeFromListIfExists(&head,&tail,nums[i]) == 0)
            addToList(&head,&tail,nums[i]);
    }
    return head->num;
}

void addToList(List *head, List *tail, int n){
    if(*head == NULL){
        *head = (List)malloc(sizeof(struct Node));
        (*head)->num = n;
        (*head)->next = *tail;
    }
    else if(*head != NULL && *tail == NULL){
        *tail = (List)malloc(sizeof(struct Node));
        (*tail)->num = n;
        (*head)->next = *tail;
        (*tail)->next = NULL;
    }
    else{
        List tmp = (List)malloc(sizeof(struct Node));
        tmp->num = n;
        tmp->next = NULL;
        (*tail)->next = tmp;
        *tail = tmp;
    }
}

int removeFromListIfExists(List *head, List *tail, int n){
    List l = *head, prev = NULL;
    while(l != NULL){
        if(l->num == n){
            if(prev == NULL){
                *head = l->next;
                if(l->next==NULL)
                    *tail = NULL;
            }
            else{
                prev->next = l->next;
                if(l->next == NULL)
                    *tail = prev;
            }
            free(l);
            return 1;
        }
        else
            prev = l;
        l = l->next;
    }
    return 0;
}

void printList(List head){
    List l = head;
    while(l != NULL){
        printf("[%d]",l->num);
        l = l->next;
        if(l != NULL)
            printf("->");
    }
}