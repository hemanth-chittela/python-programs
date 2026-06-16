name={"city":"hyderabad","town":"muthangi","food":{"chicken":"food","mutton":"food","items":
      ["tape","shoes","computer"]}}
print(name)

name={
       "city":"hyderabad",
       "town":"muthangi",
       "food":                    # for food we have opened a dictonary
                {
                "chicken":"food",
                "mutton":"food",
                "items":          # here we are giving the list of items 
                # to make this into yaml we need to remove = , [ ] { and } and that's it now it is yaml
                # coming to yaml we can also remove " " which we know because we are already writing the yml scripts
                        [
                         "tape",
                         "shoes",
                         "computer"
                        ]
                }
}
print(name)